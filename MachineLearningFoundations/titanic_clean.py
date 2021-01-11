import pandas
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt


titanic=pd.read_csv("titanic.csv")
titanic.drop(['Name','Ticket'],axis=1,inplace=True)
titanic.head()
#create indcator for Cabin
titanc['Cabin_ind']=np.where(titanic['Cabin'].isnull(), 0,1)
#convert sex to numerical
gender={'male':0,'female':1}
titanic['Sex']=titanic['Sex'].map(gendere)

#drop Cabin and Embarked
titanic.drop(['Cabin','Enbarked'],axis=1,inplace=True)
