import pandas
import gensim
import numpy as np


from sklearn.model_selection import train_test_split
messages=pd.read_csv("data/spam.csv", encoding="latin-1")
messages=messages.drop(labels=['Unnamed: 2','Unnamed: 3','Unnamed: 4'],axis=1)
messages.columns=['label','text']
messages['text_clean']=messages['text'].apply(lambda x:gensim.utils.simple_preprocess(x))
X_train,X_test,y_train,y_test=train_test_split(messages['text_clean'],messages['label'],test_size=0.2)

#Doc2Vec requires the documents to be tagged
tagged_docs=[ gensim.models.doc2vec.TaggedDocument(v,[i]) for i,v in enumerate(X_train)]
#Training the model
d2v_model=gensim.models.Doc2Vec(tagged_docs,vector_size=100,window=5,min_count=2)
#making an infering
d2v_model.infer_vector(['i',' am',' learning ','nlp'])
#preparing the test data to be used in machinelearning by getting the document vectors for each sentence in X_test
vectors=[[d2v_model.infer_vector(words)]for word in X_test]
