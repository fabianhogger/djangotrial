import pandas as pd
import string
import re
import nltk
pd.set_option('display.max_colwidth',100)
df=pd.read_csv("SMSSpamCollection.tsv",sep="\t",header=None)
df.columns=['label','body_text']
stopwords=nltk.corpus.stopwords.words('english')
ps=nltk.PorterStemmer()


def clean_text(text):
    text=''.join([char for char in text if char not in string.punctuation])
    tokens=re.split('\W+',text)
    text=' '.join([ps.stem(word) for word in tokens if word not in stopwords])#returns a string for n-gram
    return text
df["clean_text"]=df['body_text'].apply(lambda x: clean_text(x))
print(df.head())
