import pandas as pd
data=pd.read_csv('abcnews-date-text.csv', error_bad_lines=False)
data_text=data[['headline_text']]
data_text['index']=data_text.index
documents=data_text
