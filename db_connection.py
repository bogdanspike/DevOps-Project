import os
import psycopg2

names = []

host = os.environ['host']
user = os.environ['user']
dbname = os.environ['dbname']
password = os.environ['password']
sslmode = os.environ['sslmode']

conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()

cursor.execute("SELECT * FROM name;")
rows = cursor.fetchall()

for row in rows:
    names.append(row[1])
    print("Data row = (%s, %s, )" % (str(row[0]), str(row[1])))

conn.commit()
cursor.close()
conn.close()
