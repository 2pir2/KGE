import pandas as pd

df = pd.read_csv(
    r"C:\Users\hanxu\Desktop\KGE\PrepRelation\combined_triples.csv")

triples = df[['Head', 'Relation', 'Tail']].values
tsv_file_path = r'C:\Users\hanxu\Desktop\KGE\PrepRelation\combined_triples.tsv'
with open(tsv_file_path, 'w') as f:
    for triple in triples:
        f.write('\t'.join(map(str, triple)) + '\n')
