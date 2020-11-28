import pandas as pd
data=pd.read_csv('abcnews-date-text.csv', error_bad_lines=False)
data_text=data[['headline_text']]
data_text['index']=data_text.index
documents=data_text
"""
PREPROCESSING
    TOKENIZATION
    REMOVE WORDS<3 LETTERS
    REMOVE STOPWORDS
    LEMATIZATION
    STEMMING
"""
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprossesing import STOPWORDS
from nltk.stem import WordNetLemmatizer,SnowballStemmer
from nltk.stem.porter import *
import numpy as np
np.random.seed(2018)
import nltk
nltk.download('wordnet')


def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text,pos='v'))

def preprocess(text):
    result=[]
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprossesing.STOPWORDS AND len(token)>3:
            result.append(lemmatize_stemming(token))
            return result
