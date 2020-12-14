import pandas as pd
import string
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
def clean_text(text):
    text=''.join([char.lower() for char in text if char not in string.punctuation])
    tokens=re.split('\W+',text)
    text=' '.join([ps.stem(word) for word in tokens if word not in stopwords])#returns a string for n-gram
    return text

pd.set_option('display.max_colwidth',100)
df=pd.read_csv("SMSSpamCollection.tsv",sep="\t",header=None)
df.columns=['label','body_text']
stopwords=nltk.corpus.stopwords.words('english')
ps=nltk.PorterStemmer()

df["clean_text"]=df['body_text'].apply(lambda x: clean_text(x))


print(df.head())


ngram_vect=CountVectorizer(ngram_range=(2,2))
print(ngram_vect)

X_counts=ngram_vect.fit_tranform(df['clean_text'])
print(X_counts.shape)

print(ngram_vect.get_feature_names())
