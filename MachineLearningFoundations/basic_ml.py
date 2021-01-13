import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

titanic=pd.read_csv("titanic.csv")
titanic.head()


for i,col in enumerate(['SibSp','Parch']):
    plt.figure(i)
    sns.catplot(x=col,y='Survived',data=titanic,kind='point',aspect=2, )
titanic['family_cnt']=titanic['SibSp']+titanic['Parch']
titanic.to_csv("/filapath",index=False)
