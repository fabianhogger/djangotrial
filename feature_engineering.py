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
pd.set_option('display.max_colwidth',100)
df=pd.read_csv("SMSSpamCollection.tsv",sep="\t",header=None)
df.columns=['label','body_text']
