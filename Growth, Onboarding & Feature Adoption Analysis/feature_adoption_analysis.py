import pandas as pd

file_path = "data/final_compiled_dataset.xlsx"
sheet_name = "Copy of WV - RAW"
df = pd.read_excel(file_path, sheet_name=sheet_name)

df.columns = df.columns.str.strip().str.lower()
df["date of creation"] = pd.to_datetime(df["date of creation"], errors="coerce", dayfirst=True)
df["sign_up_year"] = df["date of creation"].dt.year

total = len(df)
financials = df[df["data against financials (yes or no)"].str.lower() == "yes"]
kpi = df[df["data against kpi (yes or no)"].str.lower() == "yes"]
esop = df[df["data against esop (yes or no)"].str.lower() == "yes"]
integrations = df[df["# of active integrations"] > 0]

summary_data = pd.DataFrame({
    "Metric": [
        "Total Companies",
        "Financials Adoption (%)",
        "KPI Adoption (%)",
        "ESOP Adoption (%)",
        "Integrations Adoption (%)",
        "Average Stakeholders per Company"
    ],
    "Value": [
        total,
        round(len(financials) / total * 100, 2),
        round(len(kpi) / total * 100, 2),
        round(len(esop) / total * 100, 2),
        round(len(integrations) / total * 100, 2),
        round(df["# of stakeholders (any role)"].mean(), 2)
    ]
})

trend_df = (
    financials.groupby("sign_up_year")
    .size()
    .reset_index(name="Companies with Financial Data")
)

summary_data.to_csv("data/feature_adoption_summary.csv", index=False)
trend_df.to_csv("data/financial_data_trend.csv", index=False)

print(summary_data)
print(trend_df)
