import sqlite3

db_connection = sqlite3.connect('ej1.db')
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

db_cursor.execute("INSERT INTO Alumnos VALUES (1,'Jorge', 'Oviedo')")
db_cursor.execute("INSERT INTO Alumnos VALUES (2,'Leia', 'Organa')")
db_cursor.execute("INSERT INTO Alumnos VALUES (3,'Tigre', 'Tigrado')")
db_cursor.execute("INSERT INTO Alumnos VALUES (4,'Javier', 'Oviedo')")
db_cursor.execute("INSERT INTO Alumnos VALUES (5,'Morena', 'Caos')")
db_cursor.execute("INSERT INTO Alumnos VALUES (6,'Pilar', 'Rodriguez')")
db_cursor.execute("INSERT INTO Alumnos VALUES (7,'Luis', 'Spinetta')")
db_cursor.execute("INSERT INTO Alumnos VALUES (8,'Jose', 'Pepe')")

db_connection.commit()

db_cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'Jorge'")

filas = db_cursor.fetchall()

print(filas)


db_connection.close()

