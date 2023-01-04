import psycopg2

connection = psycopg2.connect(database="chinook")

cursor = connection.cursor()

results = cursor.fetchall()

# fecth one result, option
# results = cursor.fetchone()

connection.close()

for result in results:
    print(result)
