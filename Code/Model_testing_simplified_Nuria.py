#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from cookies_main_pipeline import full_pipeline
from cookies_main_pipeline import X_train, y_train, X_test, y_test
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from  sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import StackingRegressor

from sklearn.ensemble import AdaBoostRegressor
from sklearn.linear_model import LogisticRegression

from sklearn.ensemble import GradientBoostingRegressor
estimators = [('rf', RandomForestRegressor(max_samples=0.9, min_samples_split=3, n_estimators=200, random_state=42)),
               ('gb',GradientBoostingRegressor(criterion='mse', min_samples_split=4,
                          n_estimators=300, random_state=42)),
               ("ab",AdaBoostRegressor(n_estimators=70, random_state=42))
               
               ]
best_reg_simple = StackingRegressor(estimators=estimators_simple,
                             cv=10,
                             final_estimator=LinearRegression())
best_reg_simple.fit(X_train_preprocess, y_train)

y_pred =best_reg_simple.predict(X_test_preprocess)

mean_squared_error(y_test, y_pred, squared=False)

