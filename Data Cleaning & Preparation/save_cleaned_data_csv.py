import pandas as pd
import os

file_path = "data/deduplicated_wevestr_data.xlsx"
output_folder = "data/Cleaned_CSV_Files"
os.makedirs(output_folder, exist_ok=True)

xls = pd.ExcelFile(file_path)

for sheet in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet)
    df.to_csv(os.path.join(output_folder, f"{sheet}.csv"), index=False)

print(f"✅ CSV files saved to folder: {output_folder}")
