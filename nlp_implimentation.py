import pandas as import pd
import string


pd.set_option('display.max_colwidth',100)
df=pd.read_csv("SMSSpamCollection.tsv",sep="\t",header=None)
df.columns=['label','body_text']


#Remove punctuation
string.punctuation
def remove_punct(text)
