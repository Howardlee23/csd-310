"""
Howard Hardnett
04/11/2022
Assignment: PyTech Collection Queries
Description: The purpose of this assignment is to create new 
             documents into the pytech collection and querying
             for the existing documents.  
"""

# import statements 
from pymongo import MongoClient

#mongodb connection 
url = "mongodb+srv://admin:admin@cluster0.l5ram.mongodb.net/pytech?retryWrites=true&w=majority"

#connect to the cluster 
client = MongoClient(url)

#connect to the database 
db = client.pytech

#insert new document





#show the collection 
print("--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
print(db.list_collection_names())


# Ends the program
input("End of program, press any key to continue....")
