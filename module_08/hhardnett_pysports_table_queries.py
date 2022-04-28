# Howard Hardnett
# 04/25/2022
# Assignment: PySports: Table Queries

import mysql.connector 
from mysql.connector import errorcode

db = mysql.connector.connect(user = "root",password = "HHpw041517",host = "localhost",database = "pysports")


cursor1 = db.cursor()
	
cursor1.execute("SELECT team_id,team_name, mascot FROM team")

teams = cursor1.fetchall()
 


print("-- DISPLAYING TEAM RECORDS --")

for team in teams:
	print("\n")
	print("Team ID: {}".format(team[0]))
	print("Team Name: {}".format(team[1]))
	print("Mascot: {}".format(team[2]))


print("\n -- DISPLAYING PLAYER RECORDS --")


cursor2 = db.cursor()

cursor2.execute("SELECT player_id,first_name, last_name, team_id FROM player")

players = cursor2.fetchall()

for player in players:
	print("\n")
	print("Player ID: {}".format(player[0]))
	print("Frist Name: {}".format(player[1]))
	print("Last Name: {}".format(player[2]))
	print("Team ID: {}".format(player[3]))

input("Press enter to continue...")