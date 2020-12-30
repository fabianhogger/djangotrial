import gensim.downloader as api
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
messages=pd.read_csv("data/spam.csv", encoding="latin-1")
messages=messages.drop(labels=['Unnamed: 2','Unnamed: 3','Unnamed: 4'],axis=1)
messages.columns=['label','text']
wiki_embeddings=api.load('glove-wiki-gigaword-100')
#print(wiki_embeddings['king'])
messages['text_clean']=messages['text'].apply(lambda x:gensim.utils.simple_preprocess(x))
X_train,X_test,y_train,y_test=train_test_split(X_features,messages['label'],test_size=0.2)
