import gensim
import numpy as np
import pandas as pd

X_train=pd.read_csv('data/X_train.csv')
X_test=pd.read_csv('data/X_test.csv')
y_train=pd.read_csv('data/y_train.csv')
y_test=pd.read_csv('data/y_test.csv')


tagged_docs_train=[gensim.models.do2vec.TaggedDocument(v,[i]) for i,v in  enumerate(X_train['clean_text'])]
tagged_docs_test=[gensim.models.doc2vec.TaggedDocument(v,[i]) for i,v in enumerate(X_test['clean_text'])]
