This is the implementation of the CERM model (reference: https://arxiv.org/pdf/2103.03275.pdf). The package is extremely easy to use that only 3 lines are neeeded.


Objective: Estimate credit losses per year given a scenario with multi factors (e.g., Economic condition, Climate, Other impacts)

Usage:
1. Download the package
2. Run Model Demo.ipynb for quick start
3. Edit Sample Input.xlsx to have your own dataset




Input:
1. Exposure of the portfolio
2. Loss Given Default (LGD)
3. Transition Matrix (Probability of the rating migrate to the other rating/stay in the same rating)
4. Factors representing the condition (from ytd to year n)
5. Correlation Matrix (C)


Output:
Loss distribution per year

![Unknown](https://github.com/JackyOOOO/Multi-Factor-Risk-Modelling/assets/106862996/9abb3258-4c4b-4ac9-ba60-9065113f0ca2)


Possible Usage:
Calculate 1. Expected loss, 2. Unexpected loss/RWA, 3. Reverse Stress test

![Unknown](https://github.com/JackyOOOO/Multi-Factor-Risk-Modelling/assets/106862996/233bddcc-abaa-44e6-ba17-5721c5b02e2e)

![Unknown](https://github.com/JackyOOOO/Multi-Factor-Risk-Modelling/assets/106862996/e5abfe64-5812-4615-825b-68a97144ca68)


How to use the package:
1. from CERM Import CERM_Model
2. model = CERM_Model(PD, LGD, Rho, Macro_Param, Loan)
3. model.load
Then, we have everything including expected loss, RWA, loss distribution, etc.


Explanation:

1. Using Gaussian Copula Model to model the asset value (X)
  <img width="315" alt="Screenshot 2024-03-07 at 9 09 53 PM" src="https://github.com/JackyOOOO/Credit-Modelling/assets/106862996/f211086f-5f6a-4233-be87-953d987e5c6d">

2. By using 1, the Conditional Transition Matrix (M(Z)) per year can be obtained using the formula below
<img width="408" alt="Screenshot 2024-03-07 at 9 16 54 PM" src="https://github.com/JackyOOOO/Credit-Modelling/assets/106862996/4a1a9eb3-93b9-468b-994f-f740448ff9c7">

3. In order to cauculate 2, it is necessary to obtain 1. z, 2. a by the folowing proposal. The main idea is the idiosyncratic risk is sta- tionary but the micro-correlation and macro-correlation parameters evolve in time.
<img width="393" alt="Screenshot 2024-03-07 at 9 43 47 PM" src="https://github.com/JackyOOOO/Credit-Modelling/assets/106862996/a7a697ac-6eda-4b5b-bd66-4393dd3a2134">
