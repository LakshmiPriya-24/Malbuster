# this is to plot ecdf for test concept scenarios
import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.metrics import accuracy_score


# Load training data
elapsed_times = []
train_data_path = 'Trainset.csv'  
train_df = pd.read_csv(train_data_path)
test_data_path = 'Testset2.csv'   
test_df = pd.read_csv(test_data_path)


# Assuming 'label' is the column you want to predict
X_train = train_df.drop('label', axis=1)
y_train = train_df['label']
X_test = test_df.drop('label', axis=1)
y_test = test_df['label']

# Train a decision tree classifier (replace with your actual classifier)
clf = lgb.LGBMClassifier()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

print("Accuracy: " + str(accuracy_score(y_test, predictions)))