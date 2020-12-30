import gensim.downloader as api
import gensim
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
messages=pd.read_csv("data/spam.csv", encoding="latin-1")
messages=messages.drop(labels=['Unnamed: 2','Unnamed: 3','Unnamed: 4'],axis=1)
messages.columns=['label','text']
wiki_embeddings=api.load('glove-wiki-gigaword-100')
wiki_embeddings['king']
print("most similar to king,wikipedia",wiki_embeddings.most_similar("king"))
messages['text_clean']=messages['text'].apply(lambda x:gensim.utils.simple_preprocess(x))
X_train,X_test,y_train,y_test=train_test_split(messages['text_clean'],messages['label'],test_size=0.2)
#train word2vec model on our data
w2v_model=gensim.models.Word2Vec(X_train,size=100,window=5,min_count=2)
w2v_model.wv['king']
print("most similar to king with our dataset",w2v_model.wv.most_similar("king"))
"""
Preparing word2vec model for machine learning
"""
print(w2v_model.wv.index2word)
