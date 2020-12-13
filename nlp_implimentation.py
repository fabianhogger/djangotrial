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
    text=[word for word in tokens if word not in stopwords]
    return text
df["body_text_nonstop"]=df['body_text'].apply(lambda x: clean_text(x.lower()))
print(df.head())

#Stemming
#Using the porter Stemmer

ps=nltk.PorterStemmer()
"""
print(ps.stem('run'))
print(ps.stem('runner'))
print(ps.stem('running'))
"""
def stemming(tokenized_list):
    stemmed_list=[ps.stem(word) for word in tokenized_list]
    return stemmed_list
df["body_text_stemmed"]=df['body_text'].apply(lambda x: stemming(x))

"""
Lemmatizing
The process of grouping together the inflected forms of a word so they can be analyzed by a single term , identified by the the word's lemma
or
Using vocabulary analysis of words  aiming to remove  inflectional endings to return the dictionary form of the word
"""

"""
Stemming VS Lemmatizing

Stemming is typically faster as it usually chops up the end of the word using heuristics,
without any understanding of the context in which the word is used.
Lemmatizing is typically more accurate  as it uses more informed analysis to create groups of
 words with similar meaning based on the context around the word
 """
wn=nltk.WordNetLemmatizer()
print(ps.stem('goose'))
print(ps.stem('geese'))
print(wn.lemmatize("goose"))
print(wn.lemmatize("geese"))
def lemmatizing(tokenized_list):
    lemmatized=[wn.lemmatize(word) for word in tokenized_list]
    return lemmatized

df["body_text_lemmatized"]=df['body_text_nonstop'].apply(lambda x: lemmatizing(x))
print(df.head())
