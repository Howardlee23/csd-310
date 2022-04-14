"""
Howard Hardnett
04/13/2022
Assignment: PyTech Update
Description: The purpose of this assignment is to update a single document in the
             pytech database for the students collection. 
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


print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
# Dispaly all of the current documents. 
for all_documents in collection.find():
    print(all_documents)

print("\n")


print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
#Update and display the document ID 1007
new_update = collection.update_one({"_id":1007}, {"$set": {"last_name": "Smith"}})

display_change= collection.find_one({"_id":1007})

print(display_change)

#Prompt user to close the program 
input("End of program, press any key to continue...")