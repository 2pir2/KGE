import pandas as pd
import numpy as np

# Change this to process different csv files
file_path = r'C:\Users\hanxu\Desktop\KGE\Final_Dataset\updated_combined.tsv'

# Read the file, specifying the tab separator and handling bad lines
df = pd.read_csv(file_path, sep='\t', on_bad_lines='skip')

print(df.shape)
