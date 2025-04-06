import pandas as pd
import os

# Load cleaned data
file_path = "data/cleaned_wevestr_data.xlsx"
output_file = "data/deduplicated_wevestr_data.xlsx"
xls = pd.ExcelFile(file_path)

deduplicated_sheets = {}

for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name)
    df_deduped = df.drop_duplicates()
    deduplicated_sheets[sheet_name] = df_deduped

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    for sheet_name, df_deduped in deduplicated_sheets.items():
        df_deduped.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"✅ Deduplicated data saved to {output_file}")
