"""MEnu para una consecionaria 
cargar vehiculos
editar
eliminar
mostrar
salir
"""
autos = []
motos = []
vehiculos = []
class Vehiculo():
    def __init__(self, marca, modelo, color, combustible):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.combustible = combustible

    def __str__(self):
        return f"El vehiculo es un {self.marca}, de modelo {self.modelo}, de color {self.color}"

    def get_marca(self):
        return self.marca 

    def set_marca(self, marca):
        marca_eliminada = self.marca
        self.marca = marca
        return f"Se edito de {marca_eliminada} a: {self.marca}"  


    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        modelo_eliminada = self.modelo
        self.modelo = modelo
        return f"Se edito de {modelo_eliminada} a: {self.modelo}"    



    def get_color(self):
        return self.color

    def set_color(self, color):
        color_eliminada = self.color
        self.color = color
        return f"Se edito de {color_eliminada} a: {self.color}"    

    def get_combustible(self):
        return self.combustible

    def set_combustible(self, combustible):
        combustible_eliminada = self.combustible
        self.combustible = combustible
        return f"Se edito de {combustible_eliminada} a: {self.combustible}"    
  

class Auto(Vehiculo):
    def __init__(self, marca, modelo, color, combustible, tamaño_baul, motor):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.combustible = combustible
        self.tamaño_baul = tamaño_baul
        self.motor = motor

    def get_tamaño_baul(self):
        return self.tamaño_baul 

    def set_tamaño_baul(self, tamaño_baul):
        tamaño_baul_eliminada = self.tamaño_baul
        self.tamaño_baul = tamaño_baul
        return f"Se edito de {tamaño_baul_eliminada} a: {self.tamaño_baul}"  


def get_marca(self):
        return self.marca 

def set_marca(self, marca):
        marca_eliminada = self.marca
        self.marca = marca
        return f"Se edito de {marca_eliminada} a: {self.marca}"  


def get_motor(self):
        return self.motor

def set_motor(self, motor):
        motor_eliminada = self.motor
        self.motor= motor
        return f"Se edito de {motor_eliminada} a: {self.motor}"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, color, combustible, cilindrada, torke):
        super().__init__(marca, modelo, color, combustible)
        self.cilindrada = cilindrada
        self.torke = torke
    
    def get_cilindrada(self):
        return self.cilindrada

    def set_cilindrada(self, cilindrada):
        cilindrada_eliminada = self.cilindrada
        self.cilindrada= cilindrada
        return f"Se edito de {cilindrada_eliminada} a: {self.cilindrada}"
    
    def get_torke(self):
        return self.torke

    def set_torke(self, torke):
        torke_eliminada = self.torke
        self.torke= torke
        return f"Se edito de {torke_eliminada} a: {self.torke}"
   
def carga_vehiculos():
    print("MENU DE CARGA")
    print("1) Cargar Auto")
    print("2) Cargar Moto")
    print("3) Volver al menu principal")
    opcion = int(input("Ingrese la opcion deseada: "))
    if opcion == 1:
        marca = input("Ingrese la marca del Auto: ")
        modelo = input("Ingrese el modelo del Auto: ")
        color = input("Ingrese el color del Auto: ")
        combustible = input("Ingrese el tipo de combustible que utiliza el Auto: ")
        tamaño_baul = input("Ingrese el tamaño del baul del Auto: ")
        motor = input("Ingrese el motor del Auto: ")
        auto = Auto(marca, modelo, color, combustible, tamaño_baul, motor)
        autos.append(auto)
        vehiculos.append(auto)
        print(f"La carga de {marca} fue exitosa")
        print("Lo derivamos al menu principal")
        return menu()
    elif opcion == 2:
        marca = input("Ingrese la marca del Moto: ")
        modelo = input("Ingrese el modelo del Moto: ")
        color = input("Ingrese el color del Moto: ")
        combustible = input("Ingrese el tipo de combustible que utiliza el Moto: ")
        cilindrada = input("Ingrese el cilindrado de la Moto: ")
        torke = input("Ingrese el torke de la Moto: ")
        moto = Moto(marca, modelo, color, combustible, cilindrada, torke)
        motos.append(moto)
        vehiculos.append(moto)
        print(f"La carga de {marca} fue exitosa")
        print("Lo derivamos al menu principal")
        return menu()
    elif opcion == 3:
        print("Lo derivamos al menu principal")
        return menu()
    else:
        print("La opcion ingresada es incorrecta")
        print("Intentelo de nuevo")
        return carga_vehiculos()

def mostrar_vehiculos():
    print("MENU DE MUESTRA")
    print("1) Todos los Vehiculos")
    print("2) Autos")
    print("3) Motos")
    opcion = int(input("Ingrese la opcion deseada: "))
    if opcion == 1:
        if len(vehiculos) == 0:
            print("No hay Vehiculos para mostrar")
            print("Lo derivamos al menu principal")
            return menu()
        else:
            for valor in vehiculos:
                print(f"{vehiculos.index(valor)} - {valor.get_marca()}")
            print("Estos son todos los Vehiculos")
            print("Lo derivamos al menu principal")
            return menu()
    elif opcion == 2:
        if len(autos) == 0:
            print("No hay Autos para mostrar")
            print("Lo derivamos al menu principal")
            return menu()
        else:
            for valor in autos:
                print(f"{autos.index(valor)} - {valor.get_marca()}")

            print("Estos son todos los Vehiculos")
            print("Lo derivamos al menu principal")
            return menu()
    elif opcion == 3:
        if len(motos) == 0: 
            print("No hay Motos para mostrar")
            print("Lo derivamos al menu principal")
            return menu()
        else: 
            for valor in motos:
                print(f"{motos.index(valor)} - {valor.get_marca()}")
            
            print("Estos son todos los Vehiculos")
            print("Lo derivamos al menu principal")
            return menu()
    else:
        print("La opcion ingresada es incorrecta")
        print("Intentelo de nuevo")
        return mostrar_vehiculos()
    








def menu():

    print("MENU PRINCIPAL")
    print("1) Cargar Vehiculos")
    print("2) Mostrar Vehiculos")
    print("3) Editar Vehiculo")
    print("4) Eliminar Vehiculo")
    print("5) Salir ")
    opcion = int(input("Ingrese la opcion deseada: "))
    if opcion == 1:
        carga_vehiculos()
    elif opcion == 2:
        mostrar_vehiculos()

print("Bienvenido a la consecionaria AGUSTIN")
menu()