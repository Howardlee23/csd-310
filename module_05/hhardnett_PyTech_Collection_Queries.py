"""
Howard Hardnett
04/11/2022
Assignment: PyTech Collection Queries
Description: The purpose of this assignment it to use the find command 
             to see the documents in the collection.  
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


print("--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY--")
for all_documents in collection.find():
    print(all_documents)

print("\n")

print("--DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY--")
single_find =collection.find_one()
print(single_find)


#Ends the program
input("End of program, press any key to continue....")