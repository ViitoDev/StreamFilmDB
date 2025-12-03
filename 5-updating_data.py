import sqlite3

connection = sqlite3.connect("title.db")
cursor = connection.cursor()
id = 4
cursor.execute(
    """
        UPDATE films SET note = ?
        WHERE id = ?
    """,
    (10, id)
)

connection.commit()
print("Data update")