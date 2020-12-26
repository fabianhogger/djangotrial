import pandas as pd


def merge(file1,file2):
    df=pd.read_csv(file1)
    print(df.head())
    df2=pd.read_csv(file2)
    print(df2.head())
    f=df.merge(df2,how='outer')
    print(f.head())
merge("file1.csv","file2.csv")
