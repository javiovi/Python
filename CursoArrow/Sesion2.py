
from enum import auto

"""
mis_compras=['arroz', 'harina', 'azucar', 'yerba']
#como encontrar un elemento a traves d un indcie
mis_compras[2]

#creamos elementos en una lista
mis_compras.append('fideos')
#print(mis_compras)

mis_compras.insert(2, 'pure de tomate')
#agrega un elemento al indice indicado y desplaza el q se encuentre ocupado
#print(mis_compras)

#Borrar elementos
mis_compras.remove('harina')
#print(mis_compras)

mis_compras.pop(1) #nos permite eliminar un elemento mediante el indice, si no indicamos elementos elimina el ultimo

mis_compras.clear()
#print(mis_compras)

#articulo=input("Ingrese el articulo a comprar")
#mis_compras.append(articulo)

mis_compras.reverse()

mis_compras.sort()


#DICCIONARIOS

automovil={'Marca':'Ford', 'Modelo': 'Mustang', 'Fabricacion' : 1968}

#leer los datos de un diccionario
#print(automovil.get('Modelo'))

#print(automovil.keys())#nos mostrara todas las LLAVES CONTENIDAS
#print(automovil.values()) #nos dira todos los valores contenidos

#print(automovil.items()) #nos muestra todas las llaves y sus valores

#creacion de LLAVES CON O SIN VALOR
automovil.setdefault('color', 'verde')

#print(automovil)

#el metodo setdefault no permite actualizar una llave.
#actualizacion de LLAVES CON VALOR

automovil.update({'color':'Rojo'})
automovil.update({'Motor':'none'})
#nos permite CREAR UNA LLAVE CON UN NUEVO VALOR, EN CASO DE QUE NO EXISTA


#print(automovil)

#BORRAR LAS LLAVES



automovil.pop('modelo')#eliminamos llave y valor indicado
automovil.popitem()#eliminamos la ultima llave ingresada
automovil.clear()#elimina todas las LLAVES con sus respectivos valores




"""

#Condicionales

interruptor='On'
corriente='Fallo electrico'

#if interruptor == 'On' and  corriente == 'si':
   # print('Lamparita prendida')

#elif interruptor == 'Off' or corriente == 'no':
       # print('Lamparita apagada')

#else:
   # print('se detecto un fallo al encender la lamparita')


#bucle

respuesta = 54
while respuesta != 53:
    respuesta=int(input('cuantas lunas tiene saturno'))
    if respuesta != 53:
        print('no es la respuesta correcta')
        


#bucle for

#mis_compras=['arroz', 'Harina', 'Azucar', 'yerba']
#for articulo in mis_compras:
 #    print(articulo)

"""
compras=[]

cantidad=int(input('CUantos articulos desea comprar?: '))

for i in range(cantidad):
    articulo=input('ingrese un articulo: ')
compras.append(articulo)


print(compras)
"""