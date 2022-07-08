import math

def area_triangulo(altura: float, base: float) -> float:
    return ((altura*base)/2)

def area_circulo(radio: float) -> float:
    return (math.pi*(radio**2))

print(f"Area triangulo: {area_triangulo(10,20)}")
print(f"Area_circulo: {area_circulo(20)}")

