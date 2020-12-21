import string
import re
import nltk
import pandas as pd
def count_unique(file_path):
    df=pd.read_csv(file_path,sep=',',header=None)
    df.columns(text)
    text=''.join([char for char in df.text if char not in string.punctuation])
    print(text)
count_unique("SMSSpamCollection.tsv")
