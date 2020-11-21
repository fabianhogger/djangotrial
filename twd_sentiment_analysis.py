import pandas as pd
import re
import string
data=pd.read_csv('imdb_labelled.tsv',header=None,delimiter='\t')
data.columns=['Text','Label']
#print(data.head())
#print(data.shape)
#print(data.Label.value_counts())
def remove_punct(text):
    text_nopunct=''
    text_nopunct=re.sub('['+string.punctuation+']','',text)
    return text_nopunct
data['Text_Clean']=data['Text'].apply(lambda x: remove_punct(x))
#print(data.Text_Clean)
