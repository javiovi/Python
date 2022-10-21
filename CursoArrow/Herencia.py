class Animal():
    def __init__(self, name, species, size, sex, colour):
        self.name = name
        self.species = species
        self.size = size
        self.sex = sex
        self.colour = colour

    def __str__(self):
        return f"El animal es un {self.species}, tiene de nombre {self.name}, su sexo es {self.sex}, su presa es {self.prey}, y tiene {self.teeth}"
    
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
    

perro = Animal("Tigre", "Perro", "Grande", "Masculino", "Negro")

#hije
class Carnivoro(Animal):
    def __init__(self, name, species, size, sex, colour, prey, teeth):
        super().__init__(name, species, size, sex, colour)
        self.prey = prey
        self.teeth = teeth

    def get_prey(self):
        return self.prey

    def get_teeth(self):
        return self.teeth

    def set_prey(self, prey):
        species_fail = self.prey
        self.prey = prey
        return f"Se edito de {species_fail} a: {self.prey}"

    def set_teeth(self, teeth):
        species_fail = self.teeth
        self.teeth = teeth
        return f"Se edito de {species_fail} a: {self.teeth}"

class Mascota(Carnivoro):
    def __init__(self, name, species, size, sex, colour, prey, teeth, pelaje):
        super().__init__(name, species, size, sex, colour, prey, teeth)
        self.pelaje = pelaje

    def get_pelaje(self):
        return self.pelaje

    def set_pelaje(self, pelaje):
        species_fail = self.pelaje
        self.pelaje = pelaje
        return f"se edito {species_fail} a: {self.pelaje}"

""
leon = Carnivoro("Alex", "Felino0", "Masculino", "Marron", "Cebra", "45" )


perro= Mascota("Tigre", "Canino", "Grande", "Femenino", "Blanco", "Gato", "20", "corto")






