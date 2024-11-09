import pandas as pd
import numpy as np

def page_hinkley_test(data, threshold=50, lambda_=50, alpha=1 - 1e-4):
    mean = 0
    sum_values = 0
    m_max = -np.inf  # Negative infinity
    change_point = None

    for i, x in enumerate(data):
        sum_values += x - mean - lambda_
        mean = (1 / (i + 1)) * ((i * mean) + x)

        m_t = sum_values / (i + 1)

        if m_t > m_max:
            m_max = m_t
        elif m_max - m_t > threshold:
            change_point = i
            break

    return change_point

# Load datasets
train_data = pd.read_csv("Trainset.csv")
test_data = pd.read_csv("Testset1.csv")

# Choose relevant columns for drift detection
columns_to_check = ['orig_ip_bytes', 'orig_pkts']

# Perform Page-Hinkley test and check for drift
drift_results = {}
for col in columns_to_check:
    if test_data[col].dtype in (np.float64, np.int64):
        drift_index = page_hinkley_test(test_data[col].values)
        if drift_index is not None:
            drift_results[col] = f"Drift detected at index {drift_index}"
        else:
            drift_results[col] = "No drift detected"

# Display results
print(drift_results)