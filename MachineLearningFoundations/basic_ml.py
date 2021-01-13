import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn import train_test_split
"""PART1
titanic=pd.read_csv("titanic.csv")
titanic.head()


for i,col in enumerate(['SibSp','Parch']):
    plt.figure(i)
    sns.catplot(x=col,y='Survived',data=titanic,kind='point',aspect=2, )
titanic['family_cnt']=titanic['SibSp']+titanic['Parch']
titanic.to_csv("/titanic_cleaned.csv",index=False)
"""
"""PART2
titanic=pd.read_csv("titanic_cleaned.csv")
titanic.head()
titanc['Cabin_ind']=np.where(titanic['Cabin'].isnull(), 0,1)
gender={'male':0,'female':1}
gender={'male':0,'female':1}
titanic['Sex']=titanic['Sex'].map(gender)
cat_feat=['Cabin','Name','Ticket','Embarked']
titanic.drop(cat_feat,axis=1,inplace=True)
titanic.to_csv("/titanic_cleaned.csv",index=False)
"""

titanic=pd.read_csv("titanic_cleaned.csv")
titanic.head()
features = titanic.drop('Survived', axis=1)
labels= titanic['Survived']
x_train,x_test,y_train,y_test=train_test_split(features,labels,test_size=0.4,random_state=42)
x_train,x_val,y_train,y_val=train_test_split(x_test,y_test,test_size=0.4,random_state=42)
for dataset in [y_train,y_val,y_test]:
    print(round(len(dataset)/len(labels),2))#percentage of each dataset
x_train.to_csv("/x_train.csv",index=False)
x_test.to_csv("/x_test.csv",index=False)
y_train.to_csv("/y_train.csv",index=False)
y_test.to_csv("/y_test.csv",index=False)
x_val.to_csv("/x_val.csv",index=False)
y_val.to_csv("/y_val.csv",index=False)
