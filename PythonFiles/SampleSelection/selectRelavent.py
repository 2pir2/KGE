import pandas as pd

# Load the datasets
# Adjust file path as necessary
small_df = pd.read_csv(
    r'C:\Users\hanxu\Desktop\KGE\filtered_large_dataset.csv')
large_df = pd.read_csv(r'Final_Dataset/combined_data.csv')
# Extract unique entities from the small dataset
small_entities = set(large_df['head']).union(set(large_df['tail']))
print(len(small_entities))
# filtered_large_df = large_df[(large_df['column1'].isin(small_entities)) | (
#     large_df['column3'].isin(small_entities))]

# # Save the filtered dataset
# filtered_large_df.to_csv('filtered_large_dataset.csv', index=False)
