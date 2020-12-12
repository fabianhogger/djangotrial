from nltk.corpus import stopwords
import pandas as pd
import re
"""
#print(stopwords.words('english')[0:10])
rawData=open("SMSSpamCollection.tsv").read()
#print(rawData[:500])

parsed_data=rawData.replace("\t","\n").split("\n")
#print(parsed_data[0:10])
Label_list=parsed_data[0::2]
text_list=parsed_data[1::2]
#print(len(Label_list))
#print(len(text_list))


df=pd.DataFrame({"label":Label_list[:-1],"body_list":text_list})
print(df.head())
"""
#BETTER WAY TO HAVE READ THE SMSSpamCollection.tsv USING PANDAS

df=pd.read_csv("SMSSpamCollection.tsv",sep="\t",header=None)
df.columns=['label','body_text']
#what is the shape of the data
print("input data has {} rows and {} columns ".format(len(df),len(df.columns)))
print("out of {} rows {} are spam and {} are ham".format(len(df),len(df[df['label']=='spam']),len(df[df['label']=='ham'])))
# How much data is missing
print("Number of null in the label {}".format(len(df[df['label'].isnull()])))
print("Number of null in the data {}".format(len(df[df['body_text'].isnull()])))
re_test="this is a made up string to test 2 different regex methods "
re_test_messy="this is made up   string to  test 2   different regex methods"
re_test_messy2='this-is-made/up.string*to>>>>test----2""""""different-regex-methods'
print(re.split("\s",re_test_messy))
print(re.split("\s+",re_test_messy))
print(re.split("\W+",re_test_messy))
