import pandas as pd

data=pd.read_csv('imdb_labelled.tsv',header=None,delimiter='\t')
data.columns=['Text','Label']
df.head()
