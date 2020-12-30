import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision,recall_score
from sklearn.model_selection import train_test_split
messages=pd.read_csv("data/spam.csv", encoding="latin-1")
messages=messages.drop(labels=['Unnamed: 2','Unnamed: 3','Unnamed: 4'],axis=1)
messages.columns=['label','text']
print(messages.head())
print(messages['label'].value_counts())
print(messages.shape)
print("Number of nulls in label: {}".format(messages['label'].isnull().sum()))
print("Number of nulls in text: {}".format(messages['text'].isnull().sum()))
def clean_text(text):
    text=''.join([char for char in text if char not in string.punctuation])
    tokens=re.split('\W+',text)
    text=[word for word in tokens if word not in stopwords]
    return text
tfidf_vec=TfidfVectorizer(analyzer=clean_text)
X_tfidf=tfidf_vec.fit_transform(messages['text'])
print(X_tfidf.shape)
print(tfidf_vec.get_feature_names)
X_features=pd.DataFrame(X_tfidf.toarray())
X_train,X_test,y_train,y_test=train_test_split(X_features,messages['label'],test_size=0.2)


rf=RandomForestClassifier()
