"""
Howard Hardnett
 04/10/2022
 Assignment: mongodb_test.py
 Description: Test program for connecting to a 
              mongoDB Atlas cluster 
"""
 
# import statements 
from pymongo import MongoClient

#mongodb connection 
url = "mongodb+srv://admin:admin@cluster0.l5ram.mongodb.net/pytech?retryWrites=true&w=majority"

#connect to the cluster 
client = MongoClient(url)

#connect to the database 
db = client.pytech

#show the collection 
print("--Pytech Collection List --")
print(db.list_collection_names())
