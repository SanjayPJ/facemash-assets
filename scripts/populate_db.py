import mysql.connector
from faker import Faker
fake = Faker()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="facemash"
)


for i in range(100):
	mycursor = mydb.cursor()

	sql = "INSERT INTO participants (id, name, url, score) VALUES (%s, %s, %s, %s)"
	val = (str(i + 1), fake.name_female(), str(i) + ".jpg", str(50))
	mycursor.execute(sql, val)

	mydb.commit()

	print(mycursor.rowcount, "record inserted.")
