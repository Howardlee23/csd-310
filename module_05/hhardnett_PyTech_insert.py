"""
Howard Hardnett
04/11/2022
Assignment: PyTech Insert
Description: The purpose of this assignment is to create new 
             documents into the pytech collection and show  that they have been inserted
             into the collection.  
"""

# import statements 
from pymongo import MongoClient

#mongodb connection 
url = "mongodb+srv://admin:admin@cluster0.l5ram.mongodb.net/pytech?retryWrites=true&w=majority"

#connect to the cluster 
client = MongoClient(url)

#connect to the database 
db = client.get_database("pytech")

collection = db.get_collection("students")

#insert new documents
student_01 = {
    "_id": 1007,
    "first_name":"Michael",
    "last_name":"Scott",

}

student_02 = {
    "_id": 1008,
    "first_name":"Ronnie",
    "last_name":"Coleman",

}

student_03 = {
    "_id": 1009,
    "first_name":"James",
    "last_name":"Band",

}

#Upload the documents to Mongodb
#show the insert statements 
print("--INSERT STATEMENTS--")
michael_document = collection.insert_one(student_01).inserted_id
ronnie_document = collection.insert_one(student_02).inserted_id
james_document = collection.insert_one(student_03).inserted_id

print("Inserted student record for Michael Scott into the students colletion with document id : {}".format(michael_document))
print("Inserted student record for Ronnie Coleman into the students colletion with document id : {}".format(ronnie_document))
print("Inserted student record for James Band into the students colletion with document id : {}".format(james_document))

# Ends the program
input("End of program, press any key to continue....")
