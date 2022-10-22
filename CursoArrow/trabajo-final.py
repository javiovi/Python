
class Animales(): 
    def __init__(self, name, species, sex, colour):
     self.name  = name
     self.species = species
     self.sex = sex
     self.colour = colour 

     def __str__(self):
        return f"El animal es un {self.name}, de especie {self.species}, su sexo es {self.sex}, y su color {self.colour}"

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

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

    def set_sex(self, sex):
        sex_fail = self.sex
        self.sex = sex
        return f"Se edito de {sex_fail} a: {self.sex}"

    def set_colour(self, colour):
        colour_fail = self.colour
        self.colour = colour
        return f"Se edito de {colour_fail} a: {self.colour}"    


class Felinos(Animales): 
     def __init__(self, name, species, sex, colour, food, enemy):
         super().__init__(name, species, sex, colour)
         self.food = food
         self.enemy = enemy

     def get_food(self):
      return self.food
    
     def get_enemy(self):
        return self.enemy

     def set_food(self, food):
        species_fail = self.food
        self.food = food
        return f"Se edito de {species_fail} a: {self.food}"

     def set_enemy(self, enemy):
        species_fail = self.enemy
        self.enemy = enemy
        return f"Se edito de {species_fail} a: {self.enemy}"    

leon = Felinos("Simba","Felino", "Femenino", "Naranja", "Carne", "Hiena",)
pantera = Felinos("Mor", "Felino", "Masculino", "Negro", "Bufalos", "Serpientes")
tigre = Felinos("Tiger","Felino", "Masculino", "naranja y negro", "Zebras", "Leon")

tipos = [] 

cantidad_felinos = int(input("Ingrese el numero de felinos: "))
contador = 0

while cantidad_felinos > contador:
    name = input("Ingrese el nombre del animal: ")
    species = input("Ingrese la especie del animal: ")
    sex= input("Ingrese el sexo del animal: ")
    colour= input("Ingrese el color del animal: ")
    food = input("Ingrese que come el animal: ")
    enemy = input("Ingrese el enemigo del animal: ")
    animal = Felinos(name, species, sex, colour, food, enemy)
    tipos.append(animal)
    contador += 1

for lista in tipos:
    print(lista)