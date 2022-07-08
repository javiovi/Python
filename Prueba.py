peso = input("cual es tu peso en Kg: ")
estatura = input ("cual es tu estatura?:  ")

imc = round(float(peso)/float(estatura)**2,2)

print("tu masa corporal es:   " + str(imc))

