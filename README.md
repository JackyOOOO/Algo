This is the implementation of the CERM model.

Objective: Estimate credit losses per year given a scenario with multi factors (e.g., Economic condition, Climate, Other impacts)

Input:
1. Exposure of the portfolio
2. Loss Given Default (LGD)
3. Probability of Default (PD)
4. Factors representing the condition (from ytd to year n)
5. Correlation Matrix (C)

Output:
Loss distribution per year

Possible Usage:
Calculate 1. Expected loss, 2. Unexpected loss/RWA, 3. Reverse Stress test


Explanation:

  <img width="315" alt="Screenshot 2024-03-07 at 9 09 53 PM" src="https://github.com/JackyOOOO/Credit-Modelling/assets/106862996/f211086f-5f6a-4233-be87-953d987e5c6d">
