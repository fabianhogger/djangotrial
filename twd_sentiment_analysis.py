import pandas as pd
import re
import string
from nltk import word_tokenize
from nltk.corpus import stopwords
data=pd.read_csv('imdb_labelled.tsv',header=None,delimiter='\t')
data.columns=['Text','Label']
#print(data.head())
#print(data.shape)
#print(data.Label.value_counts())
def remove_punct(text):
    text_nopunct=''
    text_nopunct=re.sub('['+string.punctuation+']','',text)
    return text_nopunct

def lower_token(tokens):
    return [w.lower() for w in tokens]

def remove_StopWords(tokens):
    return [word for word in tokens if word not in stoplist]

data['Text_Clean']=data['Text'].apply(lambda x: remove_punct(x))
#print(data.Text_Clean)
tokens=[word_tokenize(sen) for sen in data.Text_Clean]
print("tokens: ", tokens)
lower_tokens=[lower_token(token) for token in tokens]
stoplist=stopwords.words('english')

filtered_words=[remove_StopWords(sen) for sen in lower_tokens]
data['Text_Final']=[' '.join(sen) for  sen in filtered_words]
data['tokens']=filtered_words


#ONE HOT ENCODING

pos=[]
neg=[]
for l in data.Label:
    if l ==0:
        pos.append(0)
        neg.append(1)
    else if l==1:
        pos.append(1)
        neg.append(0)
data['Pos']=pos
data['Neg']=neg

data=data[['Text_Final','tokens','Label','Pos','Neg']]
