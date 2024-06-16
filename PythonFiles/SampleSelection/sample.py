import pandas as pd
from tqdm import tqdm

# Load the list of names
names_df = pd.read_csv(r"C:\Users\hanxu\Desktop\KGE\all_link.csv")

# Assuming the list of names is in a column named 'name' in names_df
# If the column has a different name, replace 'name' with the correct column name
names_list = names_df['preprocessed_ibkh_name'].tolist()

# Load the combined data
original = pd.read_csv(
    r"C:\Users\hanxu\Desktop\KGE\Final_Dataset\combined_data.csv")

# Initialize an empty list to hold the valid rows
filtered_rows = []

# Iterate through the original dataframe with a progress bar
for index, row in tqdm(original.iterrows(), total=original.shape[0], desc="Processing"):
    if row['column1'] in names_list and row['column3'] in names_list:
        filtered_rows.append(row)

# Create a new DataFrame from the filtered rows
filtered_df = pd.DataFrame(filtered_rows)

# Save the filtered dataframe to a new CSV file
filtered_df.to_csv(
    r"C:\Users\hanxu\Desktop\KGE\Final_Dataset\filtered_combined_data.csv", index=False)

# Print the shape of the filtered dataframe to verify
print(f"Shape of filtered DataFrame: {filtered_df.shape}")
