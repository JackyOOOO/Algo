This is the implementation of the CERM model.

Objective: Estimate credit losses per year given a scenario with multi factors (e.g., Economic condition, Climate, Other impacts)

Input:
1. Exposure of the portfolio
2. Loss Given Default (LGD)
3. Transition Matrix (Probability of the rating migrate to the other rating/stay in the same rating)
4. Factors representing the condition (from ytd to year n)
5. Correlation Matrix (C)

Output:
Loss distribution per year

Possible Usage:
Calculate 1. Expected loss, 2. Unexpected loss/RWA, 3. Reverse Stress test


Explanation:

1. Using Gaussian Copula Model to model the asset value (X)
  <img width="315" alt="Screenshot 2024-03-07 at 9 09 53 PM" src="https://github.com/JackyOOOO/Credit-Modelling/assets/106862996/f211086f-5f6a-4233-be87-953d987e5c6d">

2. By using 1, the Conditional Transition Matrix (M(Z)) per year can be obtained using the formula below
<img width="408" alt="Screenshot 2024-03-07 at 9 16 54 PM" src="https://github.com/JackyOOOO/Credit-Modelling/assets/106862996/4a1a9eb3-93b9-468b-994f-f740448ff9c7">

3. In order to cauculate 2, it is necessary to obtain 1. z, 2. a by the folowing proposal.
   <img width="261" alt="Screenshot 2024-03-07 at 9 41 09 PM" src="https://github.com/JackyOOOO/Credit-Modelling/assets/106862996/c9ac787a-dda2-4c1d-85ee-8acfbdc26762">
   Where <img width="308" alt="Screenshot 2024-03-07 at 9 42 05 PM" src="https://github.com/JackyOOOO/Credit-Modelling/assets/106862996/1404bf82-5404-425b-b1b9-a78ff3776320">
<img width="131" alt="Screenshot 2024-03-07 at 9 42 25 PM" src="https://github.com/JackyOOOO/Credit-Modelling/assets/106862996/d5153673-529b-407c-a564-016867354b98">
<img width="331" alt="Screenshot 2024-03-07 at 9 42 41 PM" src="https://github.com/JackyOOOO/Credit-Modelling/assets/106862996/82c567cd-5881-44e9-b6aa-181038f3dd33">
<img width="267" alt="Screenshot 2024-03-07 at 9 42 59 PM" src="https://github.com/JackyOOOO/Credit-Modelling/assets/106862996/6dd3c1a3-a9a9-4a54-8406-ce6d3ccd1a61">


   <img width="289" alt="Screenshot 2024-03-07 at 9 40 39 PM" src="https://github.com/JackyOOOO/Credit-Modelling/assets/106862996/997f3436-f5d9-44f1-846d-8c87ee432ffa">
