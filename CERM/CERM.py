import pandas as pd
import numpy as np
from scipy.stats import norm

class CERM_Model:
    
    def __init__(self, PD, LGD, Rho, Macro_Param, Loan) :
        self.PD = PD
        self.LGD = LGD
        self.Rho = Rho
        self.Macro_Param = Macro_Param
        self.Loan = Loan
        
        # preprocessing
        self.C = np.array(Rho.iloc[:, 1:])
        self.M_reg = PD. drop(['Unnamed: 0'], axis=1)
        self.a_tilde = Macro_Param.iloc[:, 1:].values
        pass
    
    @staticmethod
    def EAD(K, r, T, t):
        if t <= T:
            return (K * ((1 + r) ** T - (1 + r) ** t) / ((1 + r) ** T - 1))
        elif t > T:
            return (0)

    def EAD_Portfolio (self, rating, t):
        data = self.Loan.loc[self.Loan['Credit Rating'] == rating]
        return (sum([self.EAD(K=data['K'].values[i], r=data['r'].values[i], T=data['T'].values[i], t=t) for i in
        range(len(data))]))
    
    @staticmethod 
    def R_reg(x):
        return (0.12 * (1 - np.exp(-50 * x)) / (1 - np.exp(-50)) + 0.24 * (
        1 - (1 - np.exp(-50 * x)) / (1 - np.exp(-50))))
    
    @property
    def load(self) :
        self.c = [np.sqrt(self.R_reg(i)) * self.a_tilde / np.sqrt(self.a_tilde[0, :] @ self.C @ self.a_tilde[0, :]) for
                    i in self.M_reg.values[:, -1]] # array per i
        self.a_reg = [np.sqrt(self.R_reg(i))*self.a_tilde[0, :] / np.sqrt(self.a_tilde[0, :] @ self.C @ self.a_tilde[0, :]) for i in self.M_reg.values[:, -1]] # array per i
        self.z_reg = pd.DataFrame(np.zeros(len(self.M_reg) ** 2). reshape(len(self.M_reg), -1))
        
        for i in range(len(self.z_reg)):
            for j in range(len(self.z_reg)):
                self.z_reg.iloc[i, j] = sum(self.M_reg.iloc[i, j:])
        self.z_reg = self.z_reg.apply(lambda x: norm. ppf(round (x, 7)))
        
        
        self.z = []
        for t in range(len(self.Macro_Param)) :
            self.z.append([self.z_reg.values[i, :] / np.sqrt(
            1 + self.c[i][t] @ self.C @ self.c[i][t].T - self.a_reg[i] @ self.C @ self.a_reg[i]) for i in
            range(len(self.z_reg))]) # array per i, t = 0
            
        self.M = []
        for t in range(len(self.Macro_Param)):
            M_t = []
            for i in range(len(self.M_reg)):
                out = []
                out.append(1 - norm.cdf(self.z[t][i][1])) #j=1
                
                if len(self.M_reg) >= 3:
                    s = -np.diff(norm.cdf(self.z[t][i]))[1:] # 2<=j<=k-1
                    for kk in s:
                        out.append(kk)
                        
                out.append(norm.cdf(self.z[t][i][-1])) # j=K
                
                M_t.append(out)
                
            self.M.append(M_t)
                                                 
        self.EL_t = [
        sum([self.M[t][i][-1] * self.EAD_Portfolio(i, 0) * self.LGD.iloc[:, 1][i] for i in range(len(self.LGD))])
        for t in range(len(self.Macro_Param))]
        
    #Conditional
    def compute_conditional(self, n_sim=2 ** 12):
        self.a = []
        for t in range (len(self.Macro_Param)):
            self.a.append([self.c[i][t] / np.sqrt(
            1 + self.c[i][t] @ self.C @ self.c[i][t].T - self.a_reg[i] @ self.C @ self.a_reg[i]) for i in
            range(len(self.c))]) # array per i, t = 0
                
        self.n_sim = n_sim
        self.RWA = []
        
        self.Z_sim = np.random.multivariate_normal(mean=np.repeat(0, len(self.C)), cov=self.C, size=self.n_sim)
        
        for t in range(len(self.z)):
            self.PD_Z = []
            
            for b in range(self.n_sim):
                M_t_sim = []
                for i in range(len(self.M_reg)):
                    out = []
                    out.append(norm.cdf((self.z[t][i][-1] - self.a[t][i] @ self.Z_sim[b]) / np.sqrt(
                    1 - self.a[t][i] @ self.C @ self.a[t][i]))) # j=K
                    M_t_sim. append (out)
                    
                self.PD_Z.append(M_t_sim)

            self.loss_sim = []
            
            for b in range(self.n_sim):
                loss_per_sim = []
                
                for initial in range(len(self.LGD)):
                    loss_per_sim.append(
                    self.PD_Z[b][initial][0] * self.EAD_Portfolio(initial, 0) * self.LGD.iloc[:, 1][initial])
                self.loss_sim.append(sum(loss_per_sim))
                
            self.RWA.append(np.quantile(self.loss_sim, 0.999) - self.EL_t[t])