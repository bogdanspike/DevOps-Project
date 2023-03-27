import psycopg2

names = []

host = "msdocs-postgresql-server-120817074.postgres.database.azure.com"
user = "azureuser@msdocs-postgresql-server-120817074"
dbname = "mypgsqldb"
password = "Pa133w0rD-120817074"
sslmode = "require"

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