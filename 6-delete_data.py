import sqlite3

connection = sqlite3.connect("title.db")
cursor = connection.cursor()
id = (4, 5)
cursor.execute(
    """
        DELETE FROM films
        WHERE ID IN (?, ?)    
    """,
    id
)

connection.commit()
print("Data successfully delete!")