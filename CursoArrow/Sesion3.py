#creacion de una funcion

"""
def bienvenida():
    nombre=input('Ingrese su nombre: ')
    print(f 'Hola {nombre}, bienvenido al curso de Python')
    print('seran 3 clases que veremos el contenido')
    print('El profesor es Sebastian')
    print('esperemos que aprendas mucho!')


    bienvenida()
"""
"""
#creacion de funcion con parametros


def matematicas(num1, num2):
    suma=num1+num2
    resta=num1-num2
    multiplicacion=num1*num2
    print(f'Resultados:\nSuma: {suma}\nResta: {resta}\nMultiplicacion: {multiplicacion}') 
    

    num1=float(input('Ingrese el primer numero:  '))
    num2=float(input('ingrese el segundo numero:  '))

matematicas (num1, num2)
"""
"""
def bienvenida(nombre,ciudad,anio,mascota):
    edad=2022-anio
    print('Hola {nombre} bienvenido a Python. TU edad es {edad}')
    print(f'Asi que eres de {ciudad}? que lindo')
    print(f'espero que {mascota} se encuentre bien')

a=input('ingrese el nombre de la mascota:  ')
b=int(input('ingrese su año de nacimiento: '))
c=input('Digame en la ciudad que vive:  ')
d=input('diganme en que ciudad vive:  ')

bienvenida(c,d,b,a)
"""
"""
#creacion funcion con return

def nota(nota1,nota2,nota3):
    promedio=(nota1+nota2+nota3)/3
    return promedio

nota_alumno=nota(1,2,3)    
  
if nota_alumno >=4:
    print('Esta Aprobado')

else:
     print('debe volver a rendir')

     """

#funcion 1: recibe una cantidad de articulos que desea comprar el usuatio y lo guarda en una lista
#funcion 2: recibe una lista, e imprime los articulos que hay quecomprar

"""
def carga_de_articulos(cantidad):
    lista=[]
    for i in range(cantidad):
        art=input('ingrese el articulo a comprar: ')
        lista.append(art)

    return lista

def art_a_comprar(listado):
    print('estos son los articulos en la lista de compra: ')
    for i in listado:
        print(i,end=',') 


cant_a_comprar=int(input('Ingrese la cantidad de articulos a comprar:  '))

listado_de_compra=carga_de_articulos(cant_a_comprar)

art_a_comprar(listado_de_compra)
"""

#funcion con return multiple
#def promedio(nota1,nota2,nota3):
 #   resultado=(nota1+nota2+nota3)/3
  #  if resultado >=4:
   #     return True,'Aprobo',resultado

    #else: 
     #   return False

#variable=promedio(4,3,2)
#print(variable)            

#un return una vez devuelto, FINALIZA LA FUNCION


#scope

def mis_numeros():
   
    resultado=numero1+numero2
    print(f'el resultado es {resultado}')

  #las variables dentro de una funcion SOLO LE PERTENECEN A LA PROPIA FUNCION y no peuden ser utilizadas aufuera
  #las variables utilizadas dentro de una funcion, pueden definirse FUERA DE ELLA, siempre y cuando SE DECLAREN ANTES D INVOCAR LA FUNCION  


numero1=9
numero2=6
mis_numeros()
