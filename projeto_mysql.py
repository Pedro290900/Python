import mysql.connector

db = mysql.connector.conect(
  host="localhost",
  user="root",
  password="password"
)

cursor = db.cursor()
sql  = 'select * from users'
cursor.execute(sql)

db.close()
