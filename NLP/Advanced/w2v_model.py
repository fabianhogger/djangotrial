import gensim
import numpy as np
import pandas as pd

X_train=pd.read_csv('data/X_train.csv')
X_test=pd.read_csv('data/X_test.csv')
y_train=pd.read_csv('data/y_train.csv')
y_test=pd.read_csv('data/y_test.csv')

#train word2vec model on X_train
w2v_model=gensim.models.Word2Vec(X_train,size=100,window=5,min_count=2)
words=set(w2v_model.wv.index2word)
X_train_vect=np.array([np.array([w2v_model.wv[i] for i in ls if i in words] for ls in X_train['clean_text']])
X_test_vect=np.array([np.array([w2v_model.wv[i] for i in ls if i in words] for ls in X_test['clean_text']])

#vrisko to meso vector
X_train_vect_avg=[]
for v in X_train_vect:
    if v.size:
        X_train_vect_avg.append(v.mean(axis=0))
    else:
        X_train_vect_avg.append(np.zeros(100,dtype=float))

X_test_vect_avg=[]
for v in X_test_vect:
    if v.size:
        X_test_vect_avg.append(v.mean(axis=0))
    else:
        X_test_vect_avg.append(np.zeros(100,dtype=float))
