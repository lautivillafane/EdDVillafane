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

if __name__ == "__main__":
    main()