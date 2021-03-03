# ML_challenge

This is a joint project done by Dirk Gruhne, Karthik Arumugam and Nuria Rius
The objective is to use different features of cookie baking to predict their quality with the highest accuracy possible (RMSE measured) without overfitting our model.

In the Data directory there are the inputs we where given. cookie.csv, the training data, and cookies_validate.csv, the training data.

In the Code directory we have the following files - 
1. fill_num_nulls.py - contains a function that imputes the null values in numeric columns with a median
2. mixin_imputer.py - contains a function that performs one hot encoding on the mixin columns.
3. cleaning_data.py - contains a function to clean the data to remove unnecessary columns, outlier rows and log transformation of some columns
4. cookies_main_pipeline.py - contains the full pipeline for imputing the null values, one hot encoding, with the column and function transformation
5. Model_testing_simplified_Nuria.ipynb - This notebook contains the final model test on the training, test data sets and the final validation data. 
