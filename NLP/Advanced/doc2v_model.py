import gensim
import numpy as np
import pandas as pd

X_train=pd.read_csv('data/X_train.csv')
X_test=pd.read_csv('data/X_test.csv')
y_train=pd.read_csv('data/y_train.csv')
y_test=pd.read_csv('data/y_test.csv')


tagged_docs_train=[gensim.models.do2vec.TaggedDocument(v,[i]) for i,v in  enumerate(X_train['clean_text'])]
tagged_docs_test=[gensim.models.doc2vec.TaggedDocument(v,[i]) for i,v in enumerate(X_test['clean_text'])]


d2v_model=gensim.models.Doc2Vec(tagged_docs_train,vector_size=100,window=5,min_count=2)
#use doc2vec to make the inputs for the algorithm

train_vectors=[d2v_model.infer_vector(v.words) for v in tagged_docs_train]
test_vectors=[d2v_model.infer_vector(v.words) for v in tagged_docs_test]


from sklearn.ensemble import RandomForestClassifier

rf=RandomForestClassifier()
rf_model=rf.fit(train_vectors,y_train.values.ravel())
y_pred=rf_model.predict(test_vectors)

from sklearn.metrics import precision_score,recall_score
precision=precision_score(y_test,y_pred)
recall=recall_score(y_test,y_pred)
print("Precision: {}, Recall: {}, Accuracy:{} ".format(round(precision,3),round(recall,3), round((y_pred==y_test['label'].sum()/len(y_pred)),3)))
