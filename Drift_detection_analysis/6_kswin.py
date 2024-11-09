import pandas as pd
from river.drift import KSWIN

# Load your CSV files
train_data = pd.read_csv('Trainset.csv')
test_data = pd.read_csv('Testset2.csv')

# Function to update KSWIN with data points and detect drift
def detect_drift(train_data, test_data, feature_column):
    kswin = KSWIN()
    drift_indices = []

    # Update KSWIN with the training data
    for value in train_data[feature_column]:
        kswin.update(value)

    # Check for drift in the test data
    for index, value in enumerate(test_data[feature_column]):
        kswin.update(value)
        if kswin.drift_detected:
            drift_indices.append(index)
            print(f"Drift detected at index {index} in feature {feature_column}")

    if not drift_indices:
        print(f"No drift detected in feature {feature_column}")
    else:
        print(f"Drift detected at indices {drift_indices} in feature {feature_column}")

# Apply drift detection on each feature column
for feature in train_data.columns:
    if feature != 'orig_ip_bytes':  # Exclude the target column
        print(f"Checking drift in feature: {feature}")
        detect_drift(train_data, test_data, feature)
