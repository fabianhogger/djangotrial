import string
import re


def clean_text(text):
    #text=''.join([char for char in text if char not in string.punctuation])#removing punctuation
    tokens=re.split('\W+',text)
    #print(tokens)
    #text=[word for word in tokens if word not in stopwords]
    return tokens

def count_unique(file_path):
    words=[]
    with open(file_path,'r') as file:

        for line in file:
            a=re.split('\W+',line)
            words+=a
    word_count=[(words.count(word)) for word in words ]

    print(words)
    print(word_count)
count_unique("file.txt")
