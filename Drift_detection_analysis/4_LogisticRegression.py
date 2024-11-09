import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

train_df = pd.read_csv('Trainset.csv')
test_df = pd.read_csv('Testset1.csv')

feature_cols = train_df.columns
target_col = 'orig_ip_bytes'

clf = LogisticRegression()
clf.fit(train_df[feature_cols], train_df[target_col])

y_pred_train = clf.predict(train_df[feature_cols])
train_accuracy = accuracy_score(train_df[target_col], y_pred_train)
print(f"Training accuracy: {train_accuracy:.3f}")

y_pred_test = clf.predict(test_df[feature_cols])
test_accuracy = accuracy_score(test_df[target_col], y_pred_test)
print(f"Test accuracy: {test_accuracy:.3f}")

if test_accuracy < train_accuracy * 0.8:  
    print("Drift detected!")
    
    drift_indices = []
    for i, (y_pred, y_true) in enumerate(zip(y_pred_test, test_df[target_col])):
        if y_pred != y_true:
            drift_indices.append(i)
    print(f"Drift indices: {drift_indices}")
else:
    print("No drift detected.")