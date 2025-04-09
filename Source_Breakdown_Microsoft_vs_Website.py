import pandas as pd

file_path = "data/final_compiled_dataset.xlsx"
sheet_name = "Copy of WV - Copy of Formatted"
df = pd.read_excel(file_path, sheet_name=sheet_name)

df["Partner"] = df["Partner"].astype(str).str.strip().str.lower()

total_companies = len(df)
microsoft_companies = df[df["Partner"] == "microsoft-for-startups"]
website_companies = df[df["Partner"] != "microsoft-for-startups"]

microsoft_percentage = (len(microsoft_companies) / total_companies) * 100
website_percentage = (len(website_companies) / total_companies) * 100

result_df = pd.DataFrame({
    "Source": ["Microsoft for Startups", "Website"],
    "Company Count": [len(microsoft_companies), len(website_companies)],
    "Percentage": [microsoft_percentage, website_percentage]
})

result_df.to_csv("data/source_breakdown_microsoft_vs_website.csv", index=False)
print(result_df)
