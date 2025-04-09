import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "data/final_compiled_dataset.xlsx"
df_raw = pd.read_excel(file_path, sheet_name="Copy of WV - RAW")
df_active_users = pd.read_excel(file_path, sheet_name="Copy of WV - Active users")

# 1. Average # of documents (companies with ≥ 1)
df_docs = df_raw[df_raw["# of documents"] > 0]
avg_docs = df_docs["# of documents"].mean()
print(f"📄 Average # of documents (≥1): {avg_docs:.2f}")

# 2. Average # of stakeholders (companies with ≥ 2)
df_stakeholders = df_raw[df_raw["# of stakeholders (any role)"] >= 2]
avg_stakeholders = df_stakeholders["# of stakeholders (any role)"].mean()
print(f"👥 Average # of stakeholders (≥2): {avg_stakeholders:.2f}")

# 3. Monthly trend of companies joining (past 12 months)
df_raw["date of creation"] = pd.to_datetime(df_raw["date of creation"], errors='coerce')
df_last_12_months = df_raw[df_raw["date of creation"] >= pd.Timestamp.now() - pd.DateOffset(months=12)]
monthly_trend = df_last_12_months["date of creation"].dt.to_period("M").value_counts().sort_index()

plt.figure(figsize=(10, 5))
monthly_trend.plot(kind='bar', color='skyblue')
plt.title("📈 Companies Joined per Month (Last 12 Months)")
plt.xlabel("Month")
plt.ylabel("Company Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visuals/monthly_joining_trend.png")
plt.close()

# 4. Companies actively updating financial/transaction data
fields = ["date last stakeholder added/ updated", "date first stakeholder added/ updated"]
df_active = df_raw.dropna(subset=fields, how='all')
active_count = df_active["company name"].nunique()
print(f"🛠️ Companies updating financial/transaction data: {active_count}")

# 5. Top industries by onboarded companies
industry_counts = df_raw["industry"].value_counts().head(10)

plt.figure(figsize=(10, 5))
industry_counts.plot(kind='bar', color='mediumseagreen')
plt.title("🏭 Top 10 Industries by Onboarded Companies")
plt.xlabel("Industry")
plt.ylabel("Company Count")
plt.tight_layout()
plt.savefig("visuals/top_industries_onboarded.png")
plt.close()

# 6. Average # of documents per industry (Top 10)
industry_avg_docs = df_docs.groupby("industry")["# of documents"].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 5))
industry_avg_docs.plot(kind='bar', color='coral')
plt.title("📄 Avg. Documents per Industry (Top 10)")
plt.xlabel("Industry")
plt.ylabel("Average Documents")
plt.tight_layout()
plt.savefig("visuals/avg_docs_per_industry.png")
plt.close()

# 7. Companies with active integrations
integrated_companies = df_raw[df_raw["# of active integrations"] > 0]
integration_count = integrated_companies["company name"].nunique()
print(f"🔌 Companies with active integrations: {integration_count}")

# 8. Retention Rate (based on login activity)
active_users = df_active_users[
    (df_active_users["Login times last 3 months"] > 0) |
    (df_active_users["Login times last 30 days"] > 0)
]
retention_rate = (len(active_users) / len(df_active_users)) * 100
print(f"🔁 Retention Rate: {retention_rate:.2f}%")
