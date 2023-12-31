"""Ejercicio 1.
Genere una lista vacía que luego se irá llenando según lo que ingrese el
usuario. Pedir los siguientes datos:
Nro de sucursal
Nombre de sucursal
Cantidad de ventas
Venta total de la sucursal

Se deberá sacar el promedio de ventas en pesos de esa sucursal

Cuando el usuario ingrese un 0 como nro de sucursal se deberá imprimir:
Todos los datos ingresados
El promedio de cada sucursal
El total vendido por toda la cadena"""

def main():
    lista = []
    nro_suc = int(input("Ingrese el nro de sucursal: "))
    while nro_suc != 0:
        nom_suc = input("Ingrese el nombre de la sucursal: ")
        cant_ventas = int(input("Ingrese la cantidad de ventas: "))  
        tot_suc = int(input("Ingrese la venta total de la sucursal: "))

        lista.append([nro_suc, nom_suc,cant_ventas,tot_suc])
        
        nro_suc = int(input("Ingrese el nro de sucursal: "))

    for i in range(len(lista)):
        print(f"{lista[i]}:")
        promedio = lista[i][3]/lista[i][2]
        print(f"El promedio es: {promedio}\n")
# if __name__ == "__main__":
#     main()


"""
Ejercicio 2.
Genere un diccionario vacío que luego se irá llenando según lo que ingrese el
usuario. Pedir los siguientes datos:
ISBN
Nombre del libro
Stock
Precio del libro
Cuando el usuario ingrese un 0 como ISBN se deberá imprimir:
    - Todos los datos ingresados
    - La cantidad total de libros
    - El monto total de todos los libros
    - El valor promedio de los libros
"""

def main():
    dicc_libros = {}
    isbn = 1
    tot_libros = 0
    tot_monto = 0
    valor_promedio = 0

    while isbn != 0:
        isbn = int(input("Ingrese el ISBN del libro: "))
        if isbn != 0:
            nombre_libro = input("Ingrese el nombre del libro: ")  
            stock = int(input("Ingrese el stock del libro: "))
            precio_libro = float(input("Ingrese el precio del libro: "))
            dicc_libros[isbn] = {
                    "nombre": nombre_libro,
                    "stock": stock,
                    "precio": precio_libro
                }
    
    for i in dicc_libros:
        tot_libros = tot_libros + dicc_libros[i]['stock']
        tot_monto = tot_monto + (dicc_libros[i]['precio'] * dicc_libros[i]['stock'])
        valor_promedio = round(tot_monto/tot_libros,2)
        print(f"{dicc_libros[i]['nombre']: }")
        print(f"- {i}\n- {dicc_libros[i]['stock']} libros\n- ${dicc_libros[i]['precio']}")
        
    # print(dicc_libros)
    print(f"En total hay {tot_libros} libros")
    print(f"El monto total es de: {tot_monto}")
    print(f"El valor promedio es de: {valor_promedio}")

# if __name__ == '__main__':
#     main()

"""
Ejercicio 3.
Implementar una función que calcule la suma de todos los números enteros
comprendidos entre cero y un número entero positivo dado.
"""
def suma_enteros(num):
    if num == 0:
        return 0
    else:
        return num + suma_enteros(num-1)
    

def main():
    num = int(input("Indique el numero: "))
    resultado = suma_enteros(num)
    print(resultado)

# if __name__ == "__main__":
#     main()

"""
Ejercicio 4.
Escribir una función recursiva que permita mostrar los valores de un vector de
atrás hacia adelante.
"""
def vector_reversa(vec,indice):
    if indice < 0:
        return  
    
    print(vec[indice])
    vector_reversa(vec, indice - 1)

def main():
    mi_vector = [1, 2, 3, 4, 5]
    vector_reversa(mi_vector, len(mi_vector) - 1)

# if __name__ == "__main__":
#     main()

    
"""
Ejercicio 5.
Implementar una función recursiva que permita recorrer una matriz y mostrar sus
valores.
"""
def recorrer_matriz(matriz, fila, columna):
    if fila == len(matriz):
        return 

    if columna == len(matriz[fila]):
        recorrer_matriz(matriz, fila + 1, 0)
    else:
        print(matriz[fila][columna])
        recorrer_matriz(matriz, fila, columna + 1)

def main():
    a = [[23,45,63],[72,81,91],[56,64,37],[34,75,26]]
    recorrer_matriz(a,0,0)
    pass

# if __name__ == "__main__":
#     main()

"""
Ejercicio 6.
Dado un nro iniciar una cuenta regresiva por medio de una función recursiva,
imprimir la cuenta y al llegar a cero imprimir por pantalla "¡Booom!".
"""
def bomba(num):
    if num < 0:
        print("¡Booom!")
        return
    else:
        print(num)
        bomba(num-1)

def main():
    num = int(input("Indique el numero para la cuenta regresiva: "))
    bomba(num)

# if __name__ == "__main__":
#     main()

"""
Ejercicio 7.
Escriba una función recursiva para contar en cuantos intentos se puede adivinar
el número de un dado.
Pasos a seguir:
Genere un nro random
Solicite al usuario que ingrese un nro
Verifique si es correcto informe que acerto en X intento
Si no acertó, cuente el intento y vuelva a solicitar el nro
"""
# Puede utilizar la siguiente librería para generar los nros random al principiodel archivo
from random import *

def juego(dado, num_usuario, cont):
    if dado == num_usuario:
        if cont>1:
            print(f"Acertó en {cont} intentos!")
        else:
            print("Acertó en un intento!")
    else:
        num_usuario = int(input("Incorrecto. Elija otro numero: "))
        juego(dado, num_usuario, cont+1)

def main():
    num_dado = randint(1,6)
    num_usuario = int(input("Indique el numero del dado: "))
    juego(num_dado, num_usuario, 1)

if __name__ == "__main__":
    main()
