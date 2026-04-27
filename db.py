#print("Here will be my db")
#print("Let,s go!")
import mariadb
from select import select

conn = mariadb.connect(
    host="84.38.180.130",
    port=3306,
    user="sahaarhip51",
    password="Sahaissaha",
    database="sahaarhip51_db",
    autocommit=False   # важно для UPDATE / DELETE
)
cursor = conn.cursor()
def show_profile(id):
    cursor.execute(
        "SELECT * FROM users WHERE id = ?",
        (id,)
    )
    return cursor.fetchone()
def show_contacts(id):
    cursor.execute(
        "SELECT * FROM contacts WHERE id =?",
        (id,)
    )
    return cursor.fetchone()
def show_messages(id):
    cursor.execute(
        "SELECT * FROM messages WHERE id =?",
        (id,)
    )
    return cursor.fetchone()
def enter_message(autor,text,chatname):
    cursor.execute(
        "INSERT INTO message (id, text, autor_id, chatname) VALUES (?, ?,?,?)",
        (id, text, autor, chatname)
    )

    conn.commit()
def change_profile(id, password, email, username, city):
    cursor.execute(
        "UPDATE users SET password = ?, email = ?, username=?, city = ? WHERE id = ?",
        ( password, email, username, city, id)
    )

    conn.commit()

def delite_contact(id):
    cursor.execute(
        "DELETE FROM contacts WHERE id = ?",
        (id,)
    )

    conn.commit()
    return "успешно удален"
def add_contact(id):
    cursor.execute(
        "INSERT INTO users (contacts) VALUES ( ? )",
        (id,)
    )
    cursor.execute(
        "INSERT INTO chats (participants) VALUES ( ? ) where id = ?",
        (id,)
    )

    conn.commit()
def delite_message(id):
    cursor.execute(
        "delete from message where id =?",
        (id,)
    )
    conn.commit()
    return "успешно!"
