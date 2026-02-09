#print("Here will be my db")
#print("Let,s go!")
import mariadb
conn = mariadb.connect(
    host="84.38.180.130",
    port=3306,
    user="sahaarhip51",
    password="Sahaissaha",
    database="sahaarhip51_db",
    autocommit=False   # важно для UPDATE / DELETE
)
cursor = conn.cursor()
