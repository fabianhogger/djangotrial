import gensim
import numpy as np
import pandas as pd

X_train=pd.read_csv('data/X_train.csv')
X_test=pd.read_csv('data/X_test.csv')
y_train=pd.read_csv('data/y_train.csv')
y_test=pd.read_csv('data/y_test.csv')


w2v_model=gensim.models.Word2Vec(X_train,size=100,window=5,min_count=2)
