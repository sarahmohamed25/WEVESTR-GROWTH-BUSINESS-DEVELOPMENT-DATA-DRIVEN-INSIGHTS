import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

file_path = "data/final_compiled_dataset.xlsx"
sheet_name = "Copy of WV - Copy of Formatted"
df = pd.read_excel(file_path, sheet_name=sheet_name)

df["SignUp Date"] = pd.to_datetime(df["SignUp Date"], errors="coerce", dayfirst=True)

cutoff_date = datetime.today() - relativedelta(months=12)
df_last_12_months = df[df["SignUp Date"] >= cutoff_date].copy()
df_last_12_months["Month"] = df_last_12_months["SignUp Date"].dt.to_period("M").astype(str)

monthly_df = df_last_12_months["Month"].value_counts().sort_index().reset_index()
monthly_df.columns = ["Month", "Company Count"]

monthly_df.to_csv("data/companies_joined_last_12_months.csv", index=False)
print("\nCompanies Joined Per Month (Past 12 Months):\n")
print(monthly_df)
