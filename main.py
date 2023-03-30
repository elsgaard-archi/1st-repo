import pandas as pd
import numpy as np
data = pd.read_csv('titanic3.csv')

data.replace('?', np.nan, inplace=True)
data=data.astype({"age":np.float64, "fare":np.float64})

import seaborn as sns
import matplotlib.pyplot as plt

fig, axs = plt.subplots(ncols=5, figsize=(20,5))
sns.violinplot(x="survived", y="age", hue="sex", data=data, ax=axs[0])
sns.pointplot(x="sibsp", y="survived", hue="sex", data=data, ax=axs[1])
sns.pointplot(x="parch", y="survived", hue="sex", data=data, ax=axs[2])
sns.pointplot(x="pclass", y="survived", hue="sex", data=data, ax=axs[3])
sns.violinplot(x="survived", y="fare", hue="sex", data=data, ax=axs[4])

data.replace({'male':1,'female':0}, inplace=True)

data.corr().abs()[["survived"]]

data['relatives']=data.apply (lambda row: int((row['sibsp']+row['parch'])>0),axis=1)
data.corr().abs()[["survived"]]

data=data[['sex', 'pclass', 'age', 'relatives', 'fare', 'survived']].dropna()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split (data[['sex', 'pclass', 'age', 'relatives', 'fare']], data.survived, test_size=0.2, random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(x_train)
X_test=sc.transform(x_test)


from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(X_train, y_train)


from sklearn import metrics
predict_test = model.predict (X_test)
print(metrics.accuracy_score(y_test, predict_test))


