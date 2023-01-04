import psycopg2

connection = psycopg2.connect(database="chinook")

cursor = connection.cursor()

# cursor.execute('SELECT * FROM "Artist"')

# cursor.execute('SELECT "Name" FROM "Artist"')

# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["The Rolling Stones"])

cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [142])

#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Cher"])

results = cursor.fetchall()

# fecth one result, option
# results = cursor.fetchone()

connection.close()

for result in results:
    print(result)
