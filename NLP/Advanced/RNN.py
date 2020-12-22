import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
ps.set_option('display_max_colwidth',1000)
messages=pd.read_csv("data/spam.csv",encoding='latin-1')
messages=messages.drop(labels=["Unnamed: 2","Unnamed: 3","Unnamed: 4"],axis=1)
messages.columns=['label','text']
labels=np.where(messages['label']=='spam',1,0)

X_train,X_test,y_train,y_test=train_test_split(messages['text'],labels,test_size=0.2)
