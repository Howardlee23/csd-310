# Howard Hardnett
# 04/30/2022
# Assignment: PySports: Updates & Deletes 

import mysql.connector 
from mysql.connector import errorcode

db = mysql.connector.connect(user = "root",password = "HHpw041517",host = "localhost",database = "pysports")


cursor1 = db.cursor()
cursor2 = db.cursor()
cursor3 = db.cursor()

#Insert new player
cursor1.execute("INSERT INTO player (player_id,first_name, last_name, team_id) VALUES(21,'Smeagol','Shire Folk', 1)")


cursor1.execute("SELECT player_id,first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id=team.team_id ORDER BY player_id")
players1 = cursor1.fetchall()

print("\n -- DISPLAYING PLAYERS AFTER INSERT --")

for player1 in players1:
	print("\n")
	print("Player ID: {}".format(player1[0]))
	print("Frist Name: {}".format(player1[1]))
	print("Last Name: {}".format(player1[2]))
	print("Team Name: {}".format(player1[3]))



# Player Update Section 
cursor2.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name ='Smeagol'" )


cursor2.execute("SELECT player_id,first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id=team.team_id ORDER BY player_id")
players2 = cursor2.fetchall()

print("\n -- DISPLAYING PLAYERS AFTER UPDATE --")

for player2 in players2:
	print("\n")
	print("Player ID: {}".format(player2[0]))
	print("Frist Name: {}".format(player2[1]))
	print("Last Name: {}".format(player2[2]))
	print("Team Name: {}".format(player2[3]))



#Delete Section 
cursor3.execute("DELETE FROM player WHERE first_name = 'Gollum'")


cursor3.execute("SELECT player_id,first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id=team.team_id ORDER BY player_id")
players3 = cursor3.fetchall()

print("\n -- DISPLAYING PLAYERS AFTER DELETE --")

for player3 in players3:
	print("\n")
	print("Player ID: {}".format(player3[0]))
	print("Frist Name: {}".format(player3[1]))
	print("Last Name: {}".format(player3[2]))
	print("Team Name: {}".format(player3[3]))
