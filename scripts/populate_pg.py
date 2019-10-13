import psycopg2
from faker import Faker
fake = Faker()

conn = psycopg2.connect("user='postgres' host='localhost' dbname='facemash' password='saymyname34'")

for i in range(100):
	cursor = conn.cursor()

	sql = "INSERT INTO participants (id, name, url, score) VALUES (%s, %s, %s, %s)"
	val = (str(i + 1), fake.name_female(), str(i) + ".jpg", str(50))

	cursor.execute(sql, val);

	conn.commit()
