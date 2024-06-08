import os
import pandas as pd
import numpy as np


def save_to_csvfile(triples, output_csv_file_path):
    triples_df = pd.DataFrame(triples, columns=['Head', 'Relation', 'Tail'])
    triples_df.to_csv(output_csv_file_path, index=False)


def convert_csv_to_triples_and_save(input_dir, output_dir):
    for file_name in os.listdir(input_dir):
        if file_name.startswith('updated_') and file_name.endswith('.csv'):
            input_csv_path = os.path.join(input_dir, file_name)
            df = pd.read_csv(input_csv_path)
            print(file_name)
            titles_row = df.columns
            titles = np.array(titles_row)
            subject = titles[0]
            object = titles[1]
            titles = titles[2:np.where(titles == 'Source')[0][0]]
            triples = []
            for relationTitle in titles:
                print(relationTitle)
                for _, row in df.iterrows():
                    headEntity = row[subject]
                    relation = row[relationTitle]
                    tailEntity = row[object]
                    if relation == 1:
                        triples.append((headEntity, relationTitle, tailEntity))
                    else:
                        triples.append(
                            (headEntity, "Not" + relationTitle, tailEntity))

            output_csv_file_path = os.path.join(output_dir, file_name)
            save_to_csvfile(triples, output_csv_file_path)

            # Convert the CSV file to TSV format
            df = pd.read_csv(output_csv_file_path)
            triples = df[['Head', 'Relation', 'Tail']].values
            tsv_file_path = output_csv_file_path.replace('.csv', '.tsv')
            with open(tsv_file_path, 'w') as f:
                for triple in triples:
                    f.write('\t'.join(map(str, triple)) + '\n')


input_directory = r'C:\Users\hanxu\Desktop\KGE\Relation'
output_directory = r'C:\Users\hanxu\Desktop\KGE\PrepRelation'

convert_csv_to_triples_and_save(input_directory, output_directory)
