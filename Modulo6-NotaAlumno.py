class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return "Nombre: {}, Nota: {}".format(self.nombre, self.nota)

alumno = Alumno("Javier", 8)
print(alumno)