import pandas
import gensim
import numpy as np


from sklearn.model_selection import train_test_split
messages=pd.read_csv("data/spam.csv", encoding="latin-1")
messages=messages.drop(labels=['Unnamed: 2','Unnamed: 3','Unnamed: 4'],axis=1)
messages.columns=['label','text']
messages['text_clean']=messages['text'].apply(lambda x:gensim.utils.simple_preprocess(x))
X_train,X_test,y_train,y_test=train_test_split(messages['text_clean'],messages['label'],test_size=0.2)
