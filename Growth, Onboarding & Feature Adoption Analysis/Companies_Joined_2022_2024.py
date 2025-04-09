import pandas as pd

# Load the dataset
file_path = "data/final_compiled_dataset.xlsx"
sheet_name = "Copy of WV - Copy of Formatted"
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Convert SignUp Date column to datetime
df["SignUp Date"] = pd.to_datetime(df["SignUp Date"], errors="coerce", dayfirst=True)

# Extract year and count companies per year
df["Year"] = df["SignUp Date"].dt.year
companies_by_year = df["Year"].value_counts().sort_index()

# Filter only 2022, 2023, 2024
filtered_years = companies_by_year.loc[[2022, 2023, 2024]]

# Convert to DataFrame and rename columns
filtered_df = filtered_years.reset_index()
filtered_df.columns = ["Year", "Company Count"]

# Save to CSV
filtered_df.to_csv("data/companies_joined_2022_2024.csv", index=False)

print("\nFiltered Companies Joined Per Year (2022–2024):")
print(filtered_df)
