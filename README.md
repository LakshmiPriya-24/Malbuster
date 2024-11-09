This project implements a real-time network traffic monitoring and malware detection system leveraging nfstream for network data capture, Kafka for data streaming, 
Spark for classification, and MongoDB for storing results. The kafka_producer.py script captures network packets, including features like source and destination ports, packet counts, and flow characteristics, 
which it sends to a Kafka topic​(kafka_producer). The malware_detection.py script utilizes Spark to read from Kafka, process the packet data, and classify it using a pre-trained logistic regression model. 
The classification labels are stored in MongoDB, where devices are marked as “Normal” or “Suspected” based on threshold-based criteria​(malware_detection).

The dashboard.py file provides a Streamlit dashboard to visualize device statuses. 
It queries MongoDB, displaying the number of suspected or normal cases using color-coded bar charts for easy monitoring of potential malware incidents across connected devices​(dashboard).
