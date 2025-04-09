import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

file_path = "data/final_compiled_dataset.xlsx"
sheet_name = "Copy of WV - RAW"
df = pd.read_excel(file_path, sheet_name=sheet_name)

df["date last stakeholder added/ updated"] = pd.to_datetime(df["date last stakeholder added/ updated"], errors="coerce", dayfirst=True)

today = pd.to_datetime("today")
three_months_ago = today - relativedelta(months=3)
one_month_ago = today - relativedelta(months=1)

active_3mo = df[df["date last stakeholder added/ updated"] >= three_months_ago]
active_30d = df[df["date last stakeholder added/ updated"] >= one_month_ago]
inactive = df[df["date last stakeholder added/ updated"] < three_months_ago]

total = len(df)

summary_df = pd.DataFrame({
    "Metric": ["Active (3 Months)", "Active (30 Days)", "Inactive (Churn Risk)"],
    "Company Count": [len(active_3mo), len(active_30d), len(inactive)],
    "Percentage": [len(active_3mo)/total*100, len(active_30d)/total*100, len(inactive)/total*100]
})

summary_df.to_csv("data/user_activity_trends.csv", index=False)
print(summary_df)
