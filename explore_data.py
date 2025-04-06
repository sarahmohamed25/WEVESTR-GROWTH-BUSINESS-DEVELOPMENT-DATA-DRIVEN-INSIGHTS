import pandas as pd

# Define the path to your compiled Excel file (relative path)
file_path = "Compiled_WV_Data.xlsx"

# Load Excel file
xls = pd.ExcelFile(file_path)

# Iterate through sheets and display missing value counts
for sheet in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet)
    print(f"\n📌 Missing Values in Sheet: {sheet}")
    print(df.isnull().sum())
    print("-" * 50)
