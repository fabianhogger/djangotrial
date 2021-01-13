import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selecion import cross_val_score

tr_features=pd.read_csv('train_features.csv')
tr_labels=pd.read_csv('train_labels.csv',header=None)
rf=RandomForestClassifier()
scores=cross_val_score(rf,tr_features,tr_labels,cv=5)
