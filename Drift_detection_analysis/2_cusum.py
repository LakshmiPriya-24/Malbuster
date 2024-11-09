import pandas as pd
import numpy as np

# Load the training and test datasets
train_df = pd.read_csv('Trainset.csv')
test_df = pd.read_csv('Testset1.csv')

# Define the column to monitor for drift
column_to_monitor = 'orig_ip_bytes'

# Calculate the mean and standard deviation of the training data
train_mean = train_df[column_to_monitor].mean()
train_std = train_df[column_to_monitor].std()

# Calculate the CUSUM values for the test data


cusum = np.cumsum((test_df[column_to_monitor] - train_mean) / train_std)

# Find the position of the drift (index of the maximum CUSUM value)
drift_index = np.argmax(cusum)

drift_indices = np.where(cusum > 5)[0]
print(f"Drifts detected at indices {drift_indices}!")
