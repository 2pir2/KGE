import pandas as pd

df = pd.read_csv(
    r"C:\Users\hanxu\Desktop\KGE\Final_Dataset\HeadOrTail_dataset.csv")

triples = df[['head', 'relation', 'tail']].values
tsv_file_path = r'C:\Users\hanxu\Desktop\KGE\Final_Dataset\HeadOrTail_dataset.tsv'
with open(tsv_file_path, 'w') as f:
    for triple in triples:
        f.write('\t'.join(map(str, triple)) + '\n')
