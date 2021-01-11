import pandas
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt


titanic=pd.read_csv("titanic.csv")
cont_feat=['PassengerId','Pclass','Name','Age','Parch','SibSp','Fare']
titanic.drop(cont_feat,axis=1,inplace=True)
titanic.head()

print(titanic.groupby(titanic['Cabin'].isnull()).mean())

"""
Vlepo apo pano oti gia ta atoma me null kampina
einai pio pithano na pethanan,afto m leei oti malon opios
den eixe kampina den katafere na mpei se varka
opote ftiaxno column me binary timi gia to an eixe kampina to atomo
"""
titanc['Cabin_ind']=np.where(titanic['Cabin'].isnull(), 0,1)

for i,col in enumerate(['Cabin_ind','Sex','Embarked']):
    plt.figure(i)
    sns.catplot(x=col,y='Survived',data=titanic,kind='point',aspect=2, )

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
