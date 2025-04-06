import pandas as pd

# Load the Excel file
file_path = "data/WEVESTR_DATA.xlsx"  # Replace with your actual data path
xls = pd.ExcelFile(file_path)

# Analyze missing values
for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name)
    missing_percentage = (df.isnull().sum() / len(df)) * 100

    print("\n🔹" + "=" * 50)
    print(f"🔹 Missing Value Percentage in Sheet: {sheet_name}")
    print("=" * 50)
    print(missing_percentage)
