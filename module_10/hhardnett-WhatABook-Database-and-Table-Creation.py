# Howard Hardnett
# 05/04/2022
# Assignment: WhatABook: Database and Table Creation

import mysql.connector 
from mysql.connector import errorcode

db = mysql.connector.connect(user = "whatabook_user",password = "MySQLIsGreat!",host = "localhost",database = "whatabook")


cursor1 = db.cursor()	
cursor1.execute("SELECT user_id,first_name, last_name FROM users")
users = cursor1.fetchall()
 
print("-- DISPLAYING USERS IN RECORDS --")

for user in users:
	print("\n")
	print("User ID: {}".format(user[0]))
	print("First Name: {}".format(user[1]))
	print("Last Name: {}".format(user[2]))


print("\n -- DISPLAYING WISHLISTS IN RECORDS --")


cursor2 = db.cursor()

cursor2.execute("SELECT wishlist_id,user_id, book_id FROM wishlist")

wishlist = cursor2.fetchall()

for wishes in wishlist:
	print("\n")
	print("Wishlist ID: {}".format(wishes[0]))
	print("User ID: {}".format(wishes[1]))


print("\n -- DISPLAYING BOOKS IN RECORDS --")


cursor3 = db.cursor()

cursor3.execute("SELECT book_id, book_name, details, author FROM books")

books = cursor3.fetchall()

for multipleBooks in books:
	print("\n")
	print("Book ID: {}".format(multipleBooks[0]))
	print("Book Name: {}".format(multipleBooks[1]))
	print("Details: {}".format(multipleBooks[2]))
	print("Author: {}".format(multipleBooks[3]))
	print("Book ID: {}".format(wishes[2]))


print("\n -- DISPLAYING Store(s) IN RECORDS --")


cursor4 = db.cursor()

cursor4.execute("SELECT store_id, locale FROM store")

store = cursor4.fetchall()

for whatABookStores in store:
	print("\n")
	print("Store ID: {}".format(whatABookStores[0]))
	print("Location: {}".format(whatABookStores[1]))	

input("Press enter to continue...")