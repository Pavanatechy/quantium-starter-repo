import pandas as pd

# Read CSV files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine all files
df = pd.concat([df1, df2, df3])

# Keep only Pink Morsels
df = df[df["product"] == "pink morsel"]

# Remove dollar sign and convert price to float
df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)

# Create sales column
df["sales"] = df["quantity"] * df["price"]

# Keep only required columns
df = df[["sales", "date", "region"]]

# Save cleaned file
df.to_csv("formatted_sales_data.csv", index=False)

print("Formatted file created successfully!")