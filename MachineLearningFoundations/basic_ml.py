import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
"""
titanic=pd.read_csv("titanic.csv")
titanic.head()


for i,col in enumerate(['SibSp','Parch']):
    plt.figure(i)
    sns.catplot(x=col,y='Survived',data=titanic,kind='point',aspect=2, )
titanic['family_cnt']=titanic['SibSp']+titanic['Parch']
titanic.to_csv("/titanic_cleaned.csv",index=False)
"""
titanic=pd.read_csv("titanic_cleaned.csv")
titanic.head()
titanc['Cabin_ind']=np.where(titanic['Cabin'].isnull(), 0,1)
gender={'male':0,'female':1}
gender={'male':0,'female':1}
titanic['Sex']=titanic['Sex'].map(gender)
cat_feat=['Cabin','Name','Ticket','Embarked']
titanic.drop(cat_feat,axis=1,inplace=True)
titanic.to_csv("/titanic_cleaned.csv",index=False)
