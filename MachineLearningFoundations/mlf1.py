import pandas
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt


titanic=pd.read_csv("titanic.csv")
cat_feat=['PassengerId','Name','Ticket','Sex','Cabin','Embarked']
titanic.drop(cat_feat,axis=1,inplace=True)
titanic.head()

print(titanic.groupby('Survived').mean())

print(titanic.groupby(titanic['Age'].isnull()).mean())
for i in ['Age','Fare']:
    died=list(titanic[titanic['Survived']==0][i].dropna())
    survived=list(titanic[titanic['Survived']==1][i].dropna())
    xmin=min(min(died),min(survived))
    xmax=max(max(died),max(survived))
    width=(xmax-xmin)/40
    sns.displot(died,color='r',kde=False,bins=np.arange(xmin,xmax,width))
    sns.displot(survived,color='g',kde=False,bins=np.arange(xmin,xmax,width))
    plt.legend(['did not survive','Survived'])
    plt.title('Overlaid histogram for {}'.format(i))
    plt.show()

for i,col in enumerate(['Pclass','SibSp','Parch']):
    plt.figure(i)
    sns.catplot(x=col,y='Survived',data=titanic,kind='point',aspect=2, )

titanic['family_cnt']=titanic['SibSp']+ titanic['Parch']
#to remove model colinearity we remove SibSp and Parch
titanic.drop(['SibSp','Parch'],axis=0,inplace=True)
sns.catplot(x='family_cnt',y='Survived',data=titanic,kind='point',aspect=2,)


titanic.drop('PassengerId',axis=1,inplace=True)
#Next we replace the missing Age values with the average age
titanic['Age'].fillna(titanic['Age'].mean(),inplace=True)
