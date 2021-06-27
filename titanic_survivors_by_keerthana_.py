# -*- coding: utf-8 -*-
"""Titanic_Survivors_by_Keerthana .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ooyBOaiQhUTIGPeLsBOcloBjdAMGjdBO

# **TITANIC SURVIVOR ANALYSIS**
"""

import pandas as pd
import numpy as np

"""### READING DATA USING PANDAS

We use pandas read_csv function toread the csv file in python and pandas DataFrame method to convert file into the data frame.
"""

df = pd.DataFrame(pd.read_csv('/content/train (1).csv'))
df.head()

df.shape

"""###  Description of attributes of the dataset    
 Pclass:Passenger Class(1 = 1st;2 = 2nd;3 = 3rd)

 survival:Survival(0 = No; 1 = Yes)

 name:Name

 sex:Sex

 age:Age

 sibsp:Number of Siblings/Spouses Aboard

 parch:Number of Parents/Childern Aboard

 ticket:Ticket Number

 fare:Passenger Fare(British pound)

 cabin:Cabin

 embarked:Port of Embarkation(C= Chebourg; Q = Queenstown; S = Southampton)

### HANDELING NULL VALUES 

 The dataset may contain many rows and columns for which some values are missing, we can't leave those missing values as it is.

In such cases we have two option:

   1. Either drop the entire row or column
   2. Fill the missing values with some appropriate value let's say mean of all the values for that column may do the job.
"""

df.isnull().sum()

""" Seperating out the columns which have more than 35% of the values missing in the dataset            """

drop_col = df.isnull().sum()[df.isnull().sum()>(35/100 * df.shape[0])]
drop_col

"""**NOTE**:There is no specific number after which you should drop the column.    It's just that we decided that on our own according to what we want."""

drop_col.index

df.drop(drop_col.index, axis=1, inplace=True)
df.isnull().sum()

df.fillna(df.mean(), inplace = True)
df.isnull().sum()

"""Because ***Embarked*** contain string values,we see the details of that columnseperately from orthers as strings does not have mean and all.  """

df['Embarked'].describe()

""" For Embarked attribute, we fill the NULL values with the most frequent value in the column. """

df['Embarked'].fillna('S',inplace=True)

df.isnull().sum()

df.corr()

"""***sibsp***:Number of Sibiling/Spouse Aboard

***parch***:Number of Parent/Children Aboard 

So we can make a new column family_size by combining these two columns

"""

df['FamilySize'] = df['SibSp']+df['Parch']
df.drop(['SibSp','Parch'], axis=1, inplace=True)
df.corr()

""" **FamilySize in the ship does not have much correlence with survival rate**

Let's check if we weather the person was alone or not can affect the survival rate.
"""

df['Alone'] = [0 if df['FamilySize'][i]>0 else 1 for i in df.index]
df.head()

df.groupby(['Alone'])['Survived'].mean()

""" If the person is alone he/she has less chance of surviving.

   The reason might be the person who is travelling with his family might be belonging to rich class and might be prioritized over other.
"""

df[['Alone','Fare']].corr()

""" So we can see if the person was not alone ,the chance the ticket price is higher is high."""

df['Sex'] = [0 if df['Sex'][i]=='male' else 1 for i in df.index]
df.groupby(['Sex'])['Survived'].mean()

""" It shows,female passengers have more chance of surviving than male ones.

 It shows women were priortized over men.
"""

df.groupby(['Embarked'])['Survived'].mean()

"""## **CONCLUSION**


     

* Female passengers were prioritized over men. 
* People with high class or rich people have higher survival rate than others.The hierarichy might have been followeed while saving the passangers.


* Passengers travelling with family have higher survival rate.
* Passengers who borded the ship at Cherbourg, survived more in proportion then the others. 




 

 

 



 

 
 
 


  
"""