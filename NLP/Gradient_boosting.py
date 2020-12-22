"""
Gradient Boosting

Ensemble learning method that takes an iterative approach
to combining weak learners to create a strong learner by focusing on mistakes of prior iterations

"""
import pandas as pd
import string
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import precision_recall_fscore_support as score
def clean_text(text):
    text=''.join([char.lower() for char in text if char not in string.punctuation])
    tokens=re.split('\W+',text)
    text=[ps.stem(word) for word in tokens if word not in stopwords]
    return text
#Create  feature that show the percentage of punctuation in text
def count_punct(text):
    count=sum([1 for char in text if char in string.punctuation])
    return count/(len(text)-text.count(" "))

pd.set_option('display.max_colwidth',100)
df=pd.read_csv("SMSSpamCollection.tsv",sep="\t",header=None)
df.columns=['label','body_text']
stopwords=nltk.corpus.stopwords.words('english')
ps=nltk.PorterStemmer()

#Create A text message length feature
df['body_len']=df["body_text"].apply(lambda x:len(x)-x.count(" "))

df["punct_percent"]=df["body_text"].apply(lambda x:count_punct(x))

#TF-IDF Vectorizer
tfidf_vec=TfidfVectorizer(analyzer=clean_text)
X_tfidf=tfidf_vec.fit_transform(df['body_text'])
X_tfidf_df=pd.DataFrame(X_tfidf.toarray())
X_features=pd.concat([df['body_len'],df['punct_percent'],X_tfidf_df],axis=1)

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.model_selection import  train_test_split
def train_GB(n_est,depth,lr):
    gb=GradientBoostingClassifier(n_estimators=n_est,max_depth=depth,learning_rate=lr)
    gb_model=gb.fit(X_train,X_test)
    y_pred=gb_model.predict(X_test)
    precision,recall,fscore,support=score(y_test,y_pred,pos_label='spam',average="binary")
    print("Number Of Estimators= {},Depth= {},LR={} \n".format(n_est,depth,lr))
    print("precision={},recall={},accuracy={}".format(round(precision,3),round(recall,3),round((y_pred==y_test).sum()/len(y_test),3)))
X_train,X_test,y_train,y_test=train_test_split(X_features,df['label'],test_size=0.2)
for n_est in [50,100,150]:
    for max_depth in [3,7,11,15]:
        for lr in [0.01,0.1,1]:
            train_GB(n_est,max_depth,lr)
