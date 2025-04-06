import os
import pandas as pd

input_folder = "data/Cleaned_CSV_Files"
output_file = "data/final_compiled_dataset.xlsx"

if not os.path.exists(input_folder):
    print(f"❌ Folder not found: {input_folder}")
    exit()

with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    for file in os.listdir(input_folder):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(input_folder, file))
            sheet_name = file.replace(".csv", "")[:31]
            df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"✅ Compiled final dataset saved to {output_file}")
