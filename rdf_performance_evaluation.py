import pandas as pd
import string
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.model_selection import  train_test_split,GridSearchCV
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
X_tfidf_feat=pd.concat([df['body_len'],df['punct_percent'],X_tfidf_df],axis=1)


#Count Vectorizer
count_vect=CountVectorizer(analyzer=clean_text)
X_counts=count_vect.fit_transform(df['body_text'][:20])
X_counts_feat=pd.concat([df['body_len'],df['punct_percent'],pd.DataFrame(X_counts.toarray())],axis=1)
print(X_counts_feat.head())
print(X_tfidf_feat.head())
from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()
param={'n_estimators':[10,150,300],'max_depth':[30,60,90,None]}
gs=GridSearchCV(rf,param,cv=5,n_jobs=-1)
gs_fit=gs.fit(X_tfidf_feat,df['label'])
res=pd.DataFrame(gs_fit.cv_results_).sort_values('mean_test_score',ascending=False)[:5]
print(res)

rf=RandomForestClassifier()
gs=GridSearchCV(rf,param,cv=5,n_jobs=-1)
gs_fit=gs.fit(X_counts_feat,df['label'])
res=pd.DataFrame(gs_fit.cv_results_).sort_values('mean_test_score',ascending=False)[:5]
print(res)
