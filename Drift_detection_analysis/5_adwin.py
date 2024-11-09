import pandas as pd
from river import drift

# Load the train set CSV file
train_df = pd.read_csv('Trainset.csv')

# Load the test set CSV file
test_df = pd.read_csv('Testset2.csv')

# Define the columns to monitor for drift
#columns_to_monitor = ['orig_ip_bytes', 'orig_pkts']
columns_to_monitor = train_df.columns


# Create a list to store the ADWIN objects for each column
adwin_objects = []

# Create an ADWIN object for each column
for column in columns_to_monitor:
    adwin_objects.append(drift.ADWIN(delta=0.001))

# Initialize a list to store the drift detection results
drifts = []

# Iterate over the test set data
for i, row in test_df.iterrows():
    # Initialize a flag to indicate if a drift has been detected in any column
    drift_detected = False
    
    # Iterate over the columns to monitor
    for j, column in enumerate(columns_to_monitor):
        # Add the current test set data to the ADWIN object for this column
        adwin_objects[j].update(row[column])
        
        # Check if a drift has been detected in this column
        if adwin_objects[j].drift_detected:
            drift_detected = True
            break
    
    # If a drift has been detected in any column, append the drift detection result to the list
    if drift_detected:
        drifts.append((i, row[columns_to_monitor]))
        
        # Reset the ADWIN objects for each column
        for adwin in adwin_objects:
            adwin_objects = [drift.ADWIN(delta=0.002) for _ in columns_to_monitor]

# Print the drift detection results
for drift in drifts:
    print('Drift detected at index {}: \n{}'.format(drift[0], drift[1]))