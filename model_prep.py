import pandas as pd
import string
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.model_selection import  train_test_split
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
X_train,X_test,y_train,y_test=train_test_split(df[['body_text','body_len','punct_percent']],df['label'],test_size=0.2)

"""
The Proper way to vectorize the data is to vectorize the train data only for training and not the whole dataset
"""
#TF-IDF Vectorizer
tfidf_vec=TfidfVectorizer(analyzer=clean_text)#Empty OBject
tfidf_fit=tfidf_vec.fit(X_train['body_text'])#Fit on train data
tfidf_train=tfidf_fit.transform(X_train['body_text'])#Transform train data using the object we fit earlier
tfidf_test=tfidf_fit.transform(X_test['body_text'])#Transform the test data using the fitted object
"""
THIS is the difference with what we did earlier which was not correct
this time we have fit only on the training data so that the metrics on the test data will be closer to reality
"""
tfidf_train=pd.DataFrame(tfidf_train.toarray())
X_train_vect=pd.concat([df['body_len'],df['punct_percent'].reset_index(drop=True),tfidf_train],axis=1)
tfidf_test=pd.DataFrame(tfidf_test.toarray())
X_test_vect=pd.concat([df['body_len'],df['punct_percent'].reset_index(drop=True),tfidf_test],axis=1)