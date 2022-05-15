# Howard Hardnett
# 05/13/2022
# Module 11 Assignment: WhatABook Development 

import sys
import mysql.connector 
from mysql.connector import errorcode

db = mysql.connector.connect(user = "whatabook_user",password = "MySQLIsGreat!",host = "localhost",database = "whatabook")

#Shows the menu if called on. 
def show_menu():
	print("-- MAIN MENU --")

	print("\n 1. View Books\n 2. View Store Location & Hours\n 3. My Account\n 4. Exit Program")

	try:
		user_selection = int(input("Please select option 1, 2, 3, or 4: "))
		return user_selection
	except ValueError:
		print("That was not a valid choice. Have a great day...")
		sys.exit(0)

#Show the books in the list. 
def view_books(_cursor):
	_cursor.execute("SELECT book_id, book_name, author, details from books")

	multiple_books = _cursor.fetchall()

	print(" -- DISPLAYING BOOKS IN LISTING --")
	# use the for loop to pull all of the books from the table. 
	for show_books in multiple_books:
		print("  Book Id: {}".format(show_books[0]))
		print("  Name: {} ".format(show_books[1]))
		print("  Author: {}".format(show_books[2]))
		print("  Details: {} \n".format(show_books[3]))

#Show the location and hours of operations. 
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, store_location, store_hours from location_and_hours")

    locations = _cursor.fetchall()

    print("\n  -- DISPLAYING STORE LOCATIONS --")

    for location in locations:
        print("  Location: {}".format(location[1]))
        print("  Store Hours: {}".format(location[2]))

#validate the user's ID 
def validate_user():
	
	try:
		users_id = int(input("\nPlease select user id 1, 2, or 3: "))
		if users_id < 0 or users_id > 3:
			print("\n That was not a valid choice!")
			sys.exit(0)
		return users_id
	except ValueError:
		print("That was not a valid choice. Have a great day...")
		sys.exit(0)


def show_account_menu():
	#display the user's account menu options. 
	try:

		print(" -- CUSTOMER'S MENU -- ")
		print(" 1. Wishlist\n 2. Add Book\n 3. Main Menu")

		users_menu = int(input("\n Select option 1, 2, 3: "))

		return users_menu
	except ValueError:
		print("That was not a valid choice. Have a great day...")
		sys.exit(0)

def show_wishlist(_cursor, _user_id):
	#show the user's wishlist
	_cursor.execute("SELECT users.user_id, users.first_name, users.last_name, books.book_id, books.book_name, books.author FROM wishlist INNER JOIN users ON wishlist.user_id = users.user_id INNER JOIN books ON wishlist.book_id = books.book_id WHERE users.user_id = {}".format(_user_id))         
	users_wishlist = _cursor.fetchall()
	print("\n -- CUSTOMERS WISHLIST -- ")
	for wishes in users_wishlist:
		print("Book Name: {}".format(wishes[4]))
		print("Book Id: {}".format(wishes[3]))


def show_books_to_add(_cursor,_user_id):
	data = ("SELECT book_id, book_name, author, details FROM books WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

	print(data)

	_cursor.execute(data)

	adding_books = _cursor.fetchall()

	print(" -- AVAILABLE BOOKS -- ")

	for available_books in adding_books:
		print(" Book ID: {}".format(available_books[0]))
		print(" Book Name: {}".format(available_books[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
	_cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

#Create the code for the program 
try:
	cursor = db.cursor()
	print("\n Welcome to the WhatABook Application! ")
	print("\n")

	user_option = show_menu()
	while user_option != 4:
		
		if user_option == 1:
			view_books(cursor)
			

		if user_option == 2:
			show_locations(cursor)
			

		if user_option == 3:
			validate = validate_user()
			user_account = show_account_menu()

			while user_account !=3:

				if user_account == 1:
					show_wishlist(cursor,validate)
					print("\n")

				if user_account == 2:
					show_books_to_add(cursor,validate)

					add_new_book = int(input("\n Please type in the book's ID that you would like to add to your wishlist: "))
					add_book_to_wishlist(cursor, validate, add_new_book)
					db.commit()
					print("The book was added!!!")
				
				if user_account < 0 or user_account > 3:
					print("That is not valid option. Try again.")

				user_account = show_account_menu()
		if user_option < 0 or user_option > 4:
			print("That is not a valid option. Try again.")
		user_option = show_menu()
except mysql.connector.Error as err:

	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("  The supplied username or password are invalid")

	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("  The specified database does not exist")
	else:
		print(err)

finally:
	db.close()







	



