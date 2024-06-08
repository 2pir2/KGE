import pandas as pd
import numpy as np

file_path = r'C:\Users\hanxu\Desktop\KGE\PrepRelation\D_D_res_triples.tsv'
df = pd.read_csv(file_path, delimiter='\t', encoding='utf-8')

file_path = r"C:\Users\hanxu\Desktop\KGE\PrepRelation\updated_D_D_res.tsv"
df1 = pd.read_csv(file_path, delimiter='\t', encoding='utf-8')
print(df1.shape)
