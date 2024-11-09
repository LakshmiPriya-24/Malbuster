import streamlit as st
from pymongo import MongoClient
from time import sleep
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st_autorefresh(interval=3 * 1000, key="dataframerefresh")
def get_data_from_db():
	devices_data = {}
	resutls = {}
	mongo_client = MongoClient("mongodb://localhost:27017/")
	mongo_db = mongo_client["bda_project"]
	db_collection = mongo_db["raw_data"]
	data = db_collection.find({"remark":{"$exists":True}},{"device_name":1, "remark":1}).limit(1000)
	for collection in data:
		if collection["device_name"] not in devices_data.keys():
			devices_data[collection["device_name"]] = 0
		else:
			if collection["remark"] == 1:
				devices_data[collection["device_name"]] = devices_data[collection["device_name"]] + 1
	for device in devices_data.keys():
		if devices_data[device] > 20:# some threshold value form the calsification here greater than 20
			resutls[device] = "suspected to be infected"
		else:
			resutls[device] = "Normal"
	return resutls

def summarize_data():
	devices_data = {}
	results = {}
	mongo_client = MongoClient("mongodb://localhost:27017/")
	mongo_db = mongo_client["bda_project"]
	db_collection = mongo_db["raw_data"]
	data = db_collection.find({"remark":{"$exists":True}},{"device_name":1, "remark":1})
	for collection in data:
		if collection["device_name"] not in devices_data.keys():
			devices_data[collection["device_name"]] = 0
			results[collection["device_name"]] = [0,0,0]
		else:
			if collection["remark"] == 1:
				devices_data[collection["device_name"]] = devices_data[collection["device_name"]] + 1
				results[collection["device_name"]] = [0,results[collection["device_name"]][1] + 1,results[collection["device_name"]][2]]
			else:
				results[collection["device_name"]] = [0,results[collection["device_name"]][1],results[collection["device_name"]][2]+1]
	for device in devices_data.keys():
		if devices_data[device] > 20:
			results[device] = [1,results[device][1],results[device][2]]
		else:
			results[device] = [0,results[device][1],results[device][2]]
	return results

st.write("""
         # Malware analytics Dashboard
         """)
results = get_data_from_db()
for result in results.keys():
    st.write(f"{result} : {results[result]}")

total_data = summarize_data()
rows = []
coloums = []
colors = [] 

for device in total_data.keys():
    coloums.append(f"{device} +ve")
    rows.append(total_data[device][1])
    colors.append('red') 
    coloums.append(f"{device} -ve")
    rows.append((total_data[device][2])*(-1))
    colors.append('green')

chart_data = pd.DataFrame({"device_name":coloums,"no_of_cases":rows})

st.bar_chart(chart_data,x="device_name",y="no_of_cases")
