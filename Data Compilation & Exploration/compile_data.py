import os
import pandas as pd

# Folder where CSV files are stored
folder_path = "Data Compilation & Exploration/"
output_file = "Compiled_WV_Data.xlsx"

print(f"📂 Scanning folder: {folder_path}")
files = os.listdir(folder_path)
print("Files detected:", files)

# Create Excel writer
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    sheet_added = False

    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(".csv"):
            sheet_name = os.path.splitext(file_name)[0][:31]  # Excel sheet name max 31 chars
            file_path = os.path.join(folder_path, file_name)
            try:
                df = pd.read_csv(file_path)
                print(f"📄 Reading: {file_name}")
                print(df.head())
                if df.empty:
                    print(f"⚠️ Skipping empty file: {file_name}")
                    continue
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                sheet_added = True
            except Exception as e:
                print(f"❌ Error processing {file_name}: {e}")

    if not sheet_added:
        print("⚠️ No valid CSV files found. Adding placeholder sheet.")
        placeholder = pd.DataFrame({"Message": ["No valid CSV files found in folder."]})
        placeholder.to_excel(writer, sheet_name="Empty Data", index=False)

print(f"\n✅ Compilation complete. File saved as: {output_file}")
