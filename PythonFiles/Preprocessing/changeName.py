import os
import pandas as pd
from difflib import SequenceMatcher

# Function to find the most similar file name


def find_most_similar_file(title, file_list):
    similarity_scores = [(file, SequenceMatcher(
        None, title, file).ratio()) for file in file_list]
    most_similar_file = max(similarity_scores, key=lambda x: x[1])
    return most_similar_file[0]


# Directory containing your CSV files
relation_dir = r"C:\Users\hanxu\Desktop\KGE\Relation"
entity_dir = r"C:\Users\hanxu\Desktop\KGE\Entity"

# Load relation CSV files
relation_files = [f for f in os.listdir(relation_dir) if f.endswith('.csv')]
# Load entity CSV files
entity_files = [f for f in os.listdir(entity_dir) if f.endswith('.csv')]

# Process each relation file
for relation_file in relation_files:
    relation_df = pd.read_csv(os.path.join(relation_dir, relation_file))

    # Find the most similar entity file for each title
    column1_title = relation_df.columns[0]
    column2_title = relation_df.columns[1]
    entity_file1 = find_most_similar_file(column1_title, entity_files)
    entity_file2 = find_most_similar_file(column2_title, entity_files)

    # Load the entity files
    entity_df1 = pd.read_csv(os.path.join(entity_dir, entity_file1))
    entity_df2 = pd.read_csv(os.path.join(entity_dir, entity_file2))
    print(entity_df1)
    # Create a dictionary for DOID to name mapping
    primary_to_name1 = dict(zip(entity_df1['primary'], entity_df1['name']))
    primary_to_name2 = dict(zip(entity_df2['primary'], entity_df2['name']))

    # Replace DOID with actual names
    relation_df[column1_title] = relation_df[column1_title].map(
        primary_to_name1)
    relation_df[column2_title] = relation_df[column2_title].map(
        primary_to_name2)

    # Save the updated relation file
    relation_df.to_csv(os.path.join(
        relation_dir, f"updated_{relation_file}"), index=False)

print("Replacement completed successfully.")
