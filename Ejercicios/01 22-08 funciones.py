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

# if __name__ == "__main__":
#     main()

"""Ejercicio 4.
Realizar una función que se llame intermedio() que a partir de dos nros
devuelva el punto intermedio. Ej. El punto intermedio entre 10 y 24 = 17; entre
12 y 50 = 31.
"""

def intermedio(num1, num2):
    return (num1+num2)/2

def main():
    num1 = int(input("Indique el primer número: "))
    num2 = int(input("Indique el segundo número: "))
    print(intermedio(num1,num2))

# if __name__ == "__main__":
#     main()

"""Ejercicio 5.
Realizar una función que se llame recortar() que reciba 3 parámetros.
1º param => nro a recortar
2º param => es el límite inferior
3º param => es el límite superior
La función debe cumplir lo siguiente:
Devolver el límite inferior si el nro es menor
Devolver el límite superior si el nro es mayor
Devolver el nro si no supera los límites
"""
def recortar(nro, limite_inf, limite_sup):
    if nro < limite_inf:
        return limite_inf
    elif nro > limite_sup:
        return limite_sup
    else:
        return nro

def main():
    nro = int(input("Indique el número a recortar: "))
    lim_inf = int(input("Indique el límite inferior: "))
    lim_sup = int(input("Indique el límite superior: "))
    
    print(recortar(nro,lim_inf,lim_sup))

# if __name__ == "__main__":
#     main()

"""Ejercicio 6.
Realizar una función que se llame separar() que reciba una lista de nros y
devuelva dos listas ordenadas.
La primera con nros pares.
La segunda con nros impares."""

def separar(lista):
    num_pares = []
    num_impares = []
    for i in lista:
        if i%2 == 0:
            num_pares.append(i)
        else:
            num_impares.append(i)
    return sorted(num_pares), sorted(num_impares)

def main():
    #   Falta corregir errores, como por ej si el user pone una letra que no sea 'Y' se rompe.
    fin_bucle = "N"
    numeros = []

    print("Podés empezar a agregar numeros! Una vez que termine, escriba 'Y'")
    
    while fin_bucle == "N":
        num = input("Indique el número a agregar: ")
        if num.upper() == "Y":
            fin_bucle = "Y"
        else:
            numeros.append(int(num))
    
    listapares, listaimpares = separar(numeros)
    print(listapares,"\n",listaimpares)


if __name__ == "__main__":
    main()