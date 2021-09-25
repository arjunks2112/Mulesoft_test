import mysql.connector

conn = mysql.connector.connect(
   user='root', password='691510', host='localhost', database='mulesoft')

cursor = conn.cursor()

sql = '''SELECT * from mulesoft.favorite'''

cursor.execute(sql)

result = cursor.fetchone();
print(result)

result = cursor.fetchall();
print(result)

conn.close()
