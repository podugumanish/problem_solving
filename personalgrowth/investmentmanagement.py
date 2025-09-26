import pandas as pd

# Sample salary breakup (customizable)
monthly_salary = 150000  # example take-home salary per month (adjust as needed)

# Allocation percentages
allocation = {
    "Expenses (Rent, Food, Bills)": 0.40,   # 40%
    "Emergency Fund (until 6-9 months met)": 0.10,  # 10%
    "Short-Term Goals (1-3 yrs)": 0.10,     # 10%
    "Long-Term Growth (SIP - Equity MF)": 0.25, # 25%
    "Retirement / PPF / NPS": 0.10,         # 10%
    "Alternative Assets (REIT/Gold/Crypto)": 0.05 # 5%
}

# Calculate actual amounts
monthly_allocation = {k: v * monthly_salary for k, v in allocation.items()}

df = pd.DataFrame(list(monthly_allocation.items()), columns=["Category", "Monthly Allocation (INR)"])
df.loc[len(df.index)] = ["TOTAL", sum(monthly_allocation.values())]

import caas_jupyter_tools
caas_jupyter_tools.display_dataframe_to_user(name="Monthly Salary Allocation Plan", dataframe=df)
