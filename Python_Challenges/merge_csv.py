import pandas as pd


def merge(file1,file2,name):
    df=pd.read_csv(file1)
    df2=pd.read_csv(file2)
    f=df.merge(df2,how='outer')
    f.to_csv(path_or_buf=name)
merge("file1.csv","file2.csv")
