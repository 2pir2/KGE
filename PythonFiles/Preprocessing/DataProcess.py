import os
import pandas as pd
import numpy as np


def save_to_csvfile(triples, output_csv_file_path):
    triples_df = pd.DataFrame(triples, columns=['Head', 'Relation', 'Tail'])
    triples_df.to_csv(output_csv_file_path, index=False, encoding='utf-8')


def save_to_tsvfile(triples, output_tsv_file_path):
    with open(output_tsv_file_path, 'w', encoding='utf-8') as f:
        for triple in triples:
            f.write('\t'.join(map(str, triple)) + '\n')


def process_csv_and_convert_to_tsv(input_file_path, output_tsv_file_path):
    df = pd.read_csv(input_file_path)

    titles_row = df.columns
    titles = np.array(titles_row)
    subject = titles[0]
    object = titles[1]
    titles = titles[2:np.where(titles == 'Source')[0][0]]
    triples = []
    for relationTitle in titles:
        for _, row in df.iterrows():
            headEntity = row[subject]
            relation = row[relationTitle]
            tailEntity = row[object]
            if relation == 1:
                triples.append((headEntity, relationTitle, tailEntity))
            else:
                triples.append((headEntity, "Not" + relationTitle, tailEntity))

    output_csv_file_path = output_tsv_file_path.replace('.tsv', '.csv')
    save_to_csvfile(triples, output_csv_file_path)

    df = pd.read_csv(output_csv_file_path)
    triples = df[['Head', 'Relation', 'Tail']].values
    save_to_tsvfile(triples, output_tsv_file_path)


input_directory = r'C:\Users\hanxu\Desktop\KGE\Relation'
output_directory = r'C:\Users\hanxu\Desktop\KGE\PrepRelation'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for file_name in os.listdir(input_directory):
    if file_name.startswith('updated_') and file_name.endswith('.csv'):
        input_csv_path = os.path.join(input_directory, file_name)
        output_tsv_path = os.path.join(
            output_directory, file_name.replace('.csv', '.tsv'))
        process_csv_and_convert_to_tsv(input_csv_path, output_tsv_path)
