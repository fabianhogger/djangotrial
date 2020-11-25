import pandas as pd
import re
import string
from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from gensim.models import Word2Vec

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
    elif l==1:
        pos.append(1)
        neg.append(0)
data['Pos']=pos
data['Neg']=neg

data=data[['Text_Final','tokens','Label','Pos','Neg']]
print(data.head())







data_train,data_test=train_test_split(data,test_size=0.10,random_state=42)
all_training_words=[word for tokens in data_train['tokens'] for word in tokens]
training_sentence_lentghs=[len(tokens) for tokens in data_train['tokens']]
TRAIN_VOCAB=sorted(list(set(all_training_words)))
print("%s words total, with a vocabulary size of %s" %(len(all_training_words),len(TRAIN_VOCAB)))
print("max sentence length is %s " %max(training_sentence_lentghs))


all_test_words = [word for tokens in data_test['tokens'] for word in tokens]
test_sentence_lengths = [len(tokens) for tokens in data_test['tokens']]
TEST_VOCAB = sorted(list(set(all_test_words)))
print('%s words total, with a vocabulary size of %s' % (len(all_test_words), len(TEST_VOCAB)))
print('Max sentence length is %s' % max(test_sentence_lengths))

# Load pretrained model (since intermediate data is not included, the model cannot be refined with additional data)
model = Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True, norm_only=True)
