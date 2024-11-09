import pandas as pd
from scipy import stats

# Load the training and testing datasets
train_data = pd.read_csv('Trainset.csv')
test_data = pd.read_csv('Testset2.csv')

# Define the columns to use for the KS Test
columns_to_test = train_data.columns

# Perform the KS Test for each column
for column in columns_to_test:
    train_values = train_data[column]
    test_values = test_data[column]
    
    # Perform the KS Test
    ks_stat, p_value = stats.ks_2samp(train_values, test_values)
    
    # Print the results
    print(f"Column: {column}")
    print(f"KS Statistic: {ks_stat}")
    print(f"P-Value: {p_value}")
    
    # If the p-value is less than a certain significance level (e.g., 0.05), you can reject the null hypothesis and conclude that the distributions are different
    if p_value < 0.05:
        print(f"Drift detected in column {column}!")
    else:
        print(f"No drift detected in column {column}.")
    print()