import pandas as pd

# Replace the filename if your CSV has a different name
file_path = "E6_mosfet_output.csv"

# Read the CSV file
df = pd.read_csv(file_path)

print("Columns:")
print(df.columns)

print("\nShape:")
print(df.shape)

print("\nDescription:")
print(df.describe())
