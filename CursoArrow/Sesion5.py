class Pantera():
    def correr(self):
        return "Corro a una velocidad de 70 km/h"
    
    def comer(self):
        return "Como animales distraidos"


class Tortuga():
    def correr(self):
        return "Corro a una velocidad de 2 km/h"
    
    def comer(self):
        return "Como lechuga"


class Perro():
    def correr(self):
        return "Corro a una velocidad de 7 km/h"
    
    def comer(self):
        return "Como valanciado"
    
def animal_corre(animal):
    #agustin.correr()
    print(animal.correr())

def animal_come(animal):
    #agustin.correr()
    print(animal.comer())

animales = []
fulana = Pantera()
agustin = Tortuga()
firulais = Perro()

animales.append(fulana)
animales.append(agustin)
animales.append(firulais)
# [fulana, agustin, firulais]
for valor in animales:
    animal_corre(valor)
    print("y")
    animal_come(valor)