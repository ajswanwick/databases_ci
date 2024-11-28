import psycopg2


#connect to chinook database

connection = psycopg2.connect(database ="chinook")

#Build a Cursor object of the database
cursor = connection.cursor()

#Query1 - select all records from the "Artist" table
#cursor.execute('SELECT * FROM "Artist"')

#Query2 - select only queen from the artist table 
#cursor.execute('SELECT * FROM "Artist" WHERE "Name"= %s', ["Queen"])

cursor.execute('SELECT * FROM "Artist" WHERE "Name" =%s', ["Oasis"])

#fetch the results (multiple)
#results = cursor.fetchall()

#fetch results(single)
results = cursor.fetchone()

#close the connection
connection.close()

#print results
for result in results:
    print(result)
