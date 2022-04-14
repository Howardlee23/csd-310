"""
Howard Hardnett
04/13/2022
Assignment: PyTech Delete
Description: The purpose of this assignment is to delete a single document in the
             pytech database for the students collection. 
"""

# import statements 
from typing import Collection
from pymongo import MongoClient

#mongodb connection 
url = "mongodb+srv://admin:admin@cluster0.l5ram.mongodb.net/pytech?retryWrites=true&w=majority"

#connect to the cluster 
client = MongoClient(url)

#connect to the database 
db = client.get_database("pytech")

collection = db.get_collection("students")

# Dispaly all of the current documents.
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
 
for all_documents in collection.find():
    print(all_documents)

print("\n")

#Add a new document to the students database using the insert_one()
print("-- INSERTED STATEMENTS -- ")

studnet_04 = {
    "_id":1010,
    "first_name":"John",
    "last_name":"Doe",
}

john_document = collection.insert_one(studnet_04).inserted_id
print("Inserted student record into the students collection with document id : {}".format(john_document))

print("\n")
print("-- DISPLAYING STUDENT TEST DOC --")

new_document = collection.find_one({"_id":1010})
print(new_document)

#Delete document id 1010, and display the student collection. 
print("\n")
print("DISPLAYING STUDNETS DOCUMENTS FROM find() QUERY")

remove_document = collection.delete_one({"_id":1010})

for all_documents in collection.find():
    print(all_documents)
