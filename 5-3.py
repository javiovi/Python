def aniobisiesto():
    anio: int = int(input("Introduci en año y vamos a ver si es bisiesto    "))

    if(anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
        print(f"el año {anio} es bisiesto!")
    else:
        print(f"el año {anio} NO es bisiesto!")


print({aniobisiesto()})