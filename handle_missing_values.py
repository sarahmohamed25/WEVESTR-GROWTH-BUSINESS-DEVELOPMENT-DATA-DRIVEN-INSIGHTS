import pandas as pd
import os

# Load the Excel file
file_path = "data/WEVESTR_DATA.xlsx"
output_file = "data/cleaned_wevestr_data.xlsx"

xls = pd.ExcelFile(file_path)
cleaned_sheets = {}

for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name)

    # Drop columns with >50% missing values
    df_cleaned = df.dropna(thresh=len(df) * 0.5, axis=1)

    # Fill missing numeric with mean, categorical with mode
    df_cleaned.fillna(df_cleaned.mean(numeric_only=True), inplace=True)
    df_cleaned.fillna(df_cleaned.mode().iloc[0], inplace=True)

    cleaned_sheets[sheet_name] = df_cleaned

# Save cleaned sheets
os.makedirs("data", exist_ok=True)
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    for sheet_name, df_cleaned in cleaned_sheets.items():
        df_cleaned.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"✅ Cleaned data saved to {output_file}")
