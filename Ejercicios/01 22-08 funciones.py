"""Ejercicio 1.
Realizar una función que se llame area_rectangulo() que devuelva el área del
cuadrado a partir de su base y altura.
"""
def area_rectangulo(base, altura):
    return base*altura

def main():
    base = int(input("Indique la base del rectángulo: "))
    altura = int(input("Indique la altura del rectangulo: "))
    print(area_rectangulo(base,altura))

# if __name__ == "__main__":
#     main()

"""Ejercicio 2.
Realizar una función que se llame area_circulo() que devuelva el área del
círculo a partir de su radio.
Utilizar el valor 3.14159 como pi
"""

def area_circulo(radio):
    pi = 3.14159
    return pi*(radio**2)

def main():
    radio = int(input("Indique el radio del círculo: "))
    area = area_circulo(radio)
    print(f"El área del círculo es {area}")

# if __name__ == "__main__":
#     main()

"""Ejercicio 3.
Realizar una función que se llame relacion() que a partir de dos nros realicce
lo siguiente:
Si el primer nro es mayor que el segundo, devuelva 1
Si el primer nro es menor que el segundo, devuelva -1
Si ambos nros son iguales, devuelva 0"""

def relacion(num1, num2):
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0

def main():
    num1 = int(input("Indique el primer número a comparar: "))
    num2 = int(input("Indique el segundo número a comparar: "))
    print(relacion(num1,num2))
    
if __name__ == "__main__":
    main()
