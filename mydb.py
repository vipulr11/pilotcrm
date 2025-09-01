import mysql.connector

database = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '12345',

)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE pilotcrm")

print("Litttt")

