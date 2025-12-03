import sqlite3

conection = sqlite3.connect("title.db")
cursor = conection.cursor()
cursor.execute(
    """
        INSERT INTO films(name, year, note)
        VALUES ('Sonic', 2020, 8.0)
    """
)

conection.commit()
conection.close()
print("Insert values on table")