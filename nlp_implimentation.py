import pandas as pd
import string
import re
import nltk
pd.set_option('display.max_colwidth',100)
df=pd.read_csv("SMSSpamCollection.tsv",sep="\t",header=None)
df.columns=['label','body_text']
stopwords=nltk.corpus.stopwords.words('english')


#Remove punctuation
#string.punctuation list of punctuation types
"""
def remove_punct(text):
     text_nopunct=''.join([char for char in text if char not in string.punctuation])
     return text_nopunct
df["body_text_clean"]=df['body_text'].apply(lambda x: remove_punct(x))
#Remove Stopwords
stopwords=nltk.corpus.stopwords.words('english')

#Tokenize

def tokenize(text):
    tokens=re.split('\W+',text)
    return tokens
def remove_stopw(tokenized_list):
    nlist=[word for word in tokenized_list if word not in stopwords]
    return nlist
    
df["body_text_nonstop"]=df['boyd_text_tokenized'].apply(lambda x: remove_stopw(x))
print(df.head())

df["boyd_text_tokenized"]=df['body_text_clean'].apply(lambda x: tokenize(x.lower()))
print(df.head())
    """
def clean_text(text):
    text=''.join([char for char in text if char not in string.punctuation])
    tokens=re.split('\W+',text)
    text=[word for word in tokenized_list if word not in stopwords]
    return text


#Stemming
#Using the porter Stemmer

ps=nltk.PorterStemmer()

print(ps.stem('run'))
print(ps.stem('runner'))
print(ps.stem('running'))
