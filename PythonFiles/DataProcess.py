import pandas as pd
import numpy as np


def save_to_csvfile(triples, output_csv_file_path):
    triples_df = pd.DataFrame(triples, columns=['Head', 'Relation', 'Tail'])
    triples_df.to_csv(output_csv_file_path, index=False)


# Change this to process different csv files
file_path = r'C:\Users\hanxu\Desktop\KGE\Relation\SDSI_TC_res.csv'
df = pd.read_csv(file_path)

titles_row = df.columns
titles = np.array(titles_row)
subject = titles[0]
object = titles[1]
titles = titles[2:np.where(titles == 'Source')[0][0]]
triples = []
for relationTitle in titles:
    print(relationTitle)
    for _, row in df.iterrows():
        # Extract subject, predicate, and object from the row
        headEntity = row[subject]
        relation = row[relationTitle]
        tailEntity = row[object]
        if relation == 1:
            triples.append((headEntity, relationTitle, tailEntity))
        else:
            triples.append((headEntity, "Not" + relationTitle, tailEntity))

output_csv_file_path = r'C:\Users\hanxu\Desktop\KGE\PrepRelation\SDSI_TC_res.csv'

save_to_csvfile(triples, output_csv_file_path)

df = pd.read_csv(
    r"C:\Users\hanxu\Desktop\KGE\PrepRelation\SDSI_TC_res.csv")

triples = df[['Head', 'Relation', 'Tail']].values
tsv_file_path = r'C:\Users\hanxu\Desktop\KGE\PrepRelation\SDSI_TC_res.tsv'
with open(tsv_file_path, 'w') as f:
    for triple in triples:
        f.write('\t'.join(map(str, triple)) + '\n')
