from pickle import *

class Vehiculo:
    def __init__(self, modelo, color):
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return self.modelo + " " + self.color


vw = Vehiculo("Saveiro", "Blanca")
print(vw)

file = open('vehiculo', 'w+b')

dump(vw, file)

file.seek(0)
nuevo_vw = load(file)

print(nuevo_vw)
file.close()