import pandas as pd

file = pd.read_csv(
    "combined_triples.csv")
print(file.shape)
