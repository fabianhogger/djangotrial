"""
Feature Engineering
Creating new features or transforming your  existing features to get the most of your data
"""
"""
Transformations
Power transformations(square ,square root, etc)
Standarizing Data
"""
import pandas as pd
import string
pd.set_option('display.max_colwidth',100)
df=pd.read_csv("SMSSpamCollection.tsv",sep="\t",header=None)
df.columns=['label','body_text']

#Create A text message length feature
df['body_len']=df["body_text"].apply(lambda x:len(x)-x.count(" "))
#Create  feature that show the percentage of punctuation in text
def count_punct(text):
    count=sum([1 for char in text if char in string.punctuation])
    return count/(len(text)-text.count(" "))
df["punct_percent"]=df["body_text"].apply(lambda x:count_punct(x))
print(df["punct_percent"][:20])
