# Howard Hardnett
# 04/29/2022
# Assignment: PySports: Basic Table Joins 

import mysql.connector 
from mysql.connector import errorcode

db = mysql.connector.connect(user = "root",password = "HHpw041517",host = "localhost",database = "pysports")


cursor = db.cursor()
	
cursor.execute("SELECT player_id,first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id=team.team_id")
players = cursor.fetchall()
print("\n -- DISPLAYING PLAYER RECORDS --")


for player in players:
	print("\n")
	print("Player ID: {}".format(player[0]))
	print("Frist Name: {}".format(player[1]))
	print("Last Name: {}".format(player[2]))
	print("Team Name: {}".format(player[3]))

input("\nPress enter to continue...")