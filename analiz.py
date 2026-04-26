import warnings

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/Student_Performance.csv')

#print(df.head())
#print(df.info())

#print(df['Extracurricular Activities'].unique())
#print(df['Extracurricular Activities'].value_counts())

#sns.pairplot(df)
#plt.show()

df['Extracurricular Activities'] = df['Extracurricular Activities'].map({'Yes':1, 'No':0})

#print(df['Extracurricular Activities'].unique())

X = df.drop('Performance Index', axis=1)
y = df['Performance Index']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)


from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor(random_state=0)



param = {
    'criterion': ['squared_error', 'friedman_mse', 'poisson'],
    'splitter': ['best', 'random'],
    'max_features': ['sqrt', 'log2'],
    'max_depth': [None, 5, 10, 15, 20],
    'min_samples_split': [2, 5, 10]
}


from sklearn.model_selection import GridSearchCV

grid = GridSearchCV(estimator=DecisionTreeRegressor(random_state=0),param_grid=param, cv=5, n_jobs=-1)
grid.fit(X_train, y_train)
y_pred = grid.predict(X_test)

from sklearn.metrics import mean_absolute_error, r2_score

print(mean_absolute_error(y_test, y_pred))
print(r2_score(y_test, y_pred))









