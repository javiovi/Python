"""
lista_alumnos=[]
opcion= 'si'
while opcion != 'no':
    opcion=input('Desea cargar un alumno?')
    if opcion == 'si' :
      apellido=input('ingrese un apellido:  ')
      promedio=float(input('ingrese el promedio:  '))
      datos=(apellido,promedio)
      lista_alumnos.append(datos)

    elif opcion == 'no':
       print(lista_alumnos)

    else:
        print('opcion no valida')   


for i in lista_alumnos:

"""

diccionario={'Materia':None, 'Turno':None, 'Profesor':None}
diccionario.setdefault('Cursada')


for i in diccionario:
    valor=input(f'Ingrese el valor de {i}')
    diccionario.update({i})

print(diccionario)    

