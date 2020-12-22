import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
pd.set_option('display.max_colwidth',1000)
messages=pd.read_csv("data/spam.csv",encoding='latin-1')
messages=messages.drop(labels=["Unnamed: 2","Unnamed: 3","Unnamed: 4"],axis=1)
messages.columns=['label','text']
labels=np.where(messages['label']=='spam',1,0)
print(messages.head())
X_train,X_test,y_train,y_test=train_test_split(messages['text'],labels,test_size=0.2)

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

#Initialize and fit the tokenizer
tokenizer=Tokenizer()
tokenizer.fit_on_texts(X_train)#makes av vocabulary with an index number for every word

#Use the tokenizer to tranform the train and test sets
X_train_seq=tokenizer.text_to_sequences(X_train)#replaces the words with their indexes
X_test_seq=tokenizer.text_to_sequences(X_test)


#Padding
X_train_seq_padded=pad_sequences(X_train_seq,50)
X_test_seq_padded=pad_sequences(X_test_seq,50)
