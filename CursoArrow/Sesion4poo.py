class Animal():
    def __init__(self, name, species, size, sex, colour):
        self.name = name
        self.species = species
        self.size = size
        self.sex = sex
        self.colour = colour

    def __str__(self):
        return f"El animal es un {self.species}, tiene de nombre {self.name}, su sexo es {self.sex}"
    
    def get_name(self):
        return self.name
    
    def get_species(self):
        return self.species
    
    def get_size(self):
        return self.size
    
    def get_sex(self):
        return self.sex
    
    def get_colour(self):
        return self.colour
    
    def set_name(self, name):
        name_fail = self.name
        self.name = name
        return f"Se edito de {name_fail} a: {self.name}"
    
    def set_species(self, species):
        species_fail = self.species
        self.species = species
        return f"Se edito de {species_fail} a: {self.species}"
    

animales = []

cantidad_registros = int(input("Ingrese la cantidad de registros: "))
contador = 0

while cantidad_registros > contador:
    name = input("Ingrese el nombre del animal: ")
    species = input("Ingrese la especie del animal: ")
    size = input("Ingrese el tamaño del animal: ")
    sex = input("Ingrese el sexo del animal: ")
    colour = input("Ingrese el color del animal")
    animal = Animal(name, species, size, sex, colour)
    animales.append(animal)
    contador += 1

for valor_lista in animales:
    print(valor_lista)