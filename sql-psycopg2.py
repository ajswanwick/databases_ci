import psycopg2


#connect to chinook database

connection = psycopg2.connect(database = "chinook")

#Build a Cursor object of the database
cursor = connection.cursor()

#Query1 - select all records from the "Artist" table
cursor.execute('SELECT * FROM "Artist"')

#fetch the results (multiple)
results = cursor.fetchall()

#fetch results(single)
#results = cursor.fetchone()

#close the connection
connection.close()

#print results
for result in results:
    print(result)
