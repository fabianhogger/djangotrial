"""
Ensemble Method
Technique that creates multiple models and than combines them to produce
better results  than any of the single models individually
"""
"""
Random Forest
Constructs a collection of decision trees and then
aggregates the predictions to reach the final result
"""
import pandas as pd
import string
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
def clean_text(text):
    text=''.join([char for char in text if char not in string.punctuation])
    tokens=re.split('\W+',text)
    text=[ps.stem(word) for word in tokens if word not in stopwords]
    return text
pd.set_option('display.max_colwidth',100)
df=pd.read_csv("SMSSpamCollection.tsv",sep="\t",header=None)
df.columns=['label','body_text']
stopwords=nltk.corpus.stopwords.words('english')
ps=nltk.PorterStemmer()



#Create A text message length feature
df['body_len']=df["body_text"].apply(lambda x:len(x)-x.count(" "))
#Create  feature that show the percentage of punctuation in text
def count_punct(text):
    count=sum([1 for char in text if char in string.punctuation])
    return count/(len(text)-text.count(" "))
df["punct_percent"]=df["body_text"].apply(lambda x:count_punct(x))

tfidf_vec=TfidfVectorizer(analyzer=clean_text)
X_tfidf=tfidf_vec.fit_transform(df['body_text'])
X_tfidf_df=pd.DataFrame(X_tfidf.toarray())
X_features=pd.concat([df['body_len'],df['punct_percent'],X_tfidf_df],axis=1)
print(X_features.head())

"""
Import Kfold and cross validation

"""
from sklearn.model_selection import KFold,cross_val_score
rf=RandomForestClassifier(n_jobs=-1)
k_fold=KFold(n_splits=5)#5 subsets of data for iterations
print(cross_val_score(rf,X_features,df["label"],cv=k_fold,scoring='accuracy',n_jobs=-1))
