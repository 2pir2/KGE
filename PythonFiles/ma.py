import gzip
number_of_lines = 10
with gzip.open(r'C:\Users\hanxu\Desktop\KGE\doctests\test_unstratified_transe\training_triples\numeric_triples.tsv.gz', 'rb') as f:
    for i in range(number_of_lines):
        line = f.readline()
        print(i, line)
