import pandas as pd
import numpy as np

files = ["D_D_res_triples.csv", "D_Di_res_triples.csv", "D_Se_res_triples.csv", "Di_Di_res_triples.csv", "Di_Sy_res_triples.csv",
         "DSP_SDSI_res_triples.csv", "SDSI_A_res_triples.csv", "SDSI_D_res_triples.csv", "SDSI_Di_res_triples.csv", "SDSI_Sy_res_triples.csv", "SDSI_TC_res_triples.csv",]

dfs = []
count = 11
# Iterate over the CSV filenames and read each file into a DataFrame
for file in files:
    df = pd.read_csv(file)
    # Rename columns to ensure they are "head", "relation", "tail"
    df.columns = ["Head", "Relation", "Tail"]
    # Append the DataFrame to the list
    dfs.append(df)
    print(count)
    count -= 1

# Concatenate all the DataFrames in the list into a single DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv("combined_triples.csv", index=False)

print("All files combined into combined_triples.csv successfully.")
