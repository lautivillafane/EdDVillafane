
"""Ejercicio 1.
Pedir al usuario que ingrese un nro impar
Mientras que el usuario no ingrese un nro impar se volverá a pedir que ingrese
un nro impar
Deberá indicar por pantalla si es impar"""

def main():
    nroimp = 2
    while nroimp % 2 == 0:
        nroimp = int(input("Ingrese un numero impar: "))

    print("Tu número es ",nroimp)

if __name__ == "__main__":
    main()

"""Ejercicio 2.
Pedir al usuario que ingrese dos nros
Luego imprimir 3 opciones (1. sumar, 2. restar y 3. multiplicar)
Pedir al usuario que ingrese una opción
Verificar la opción del usuario
Mientras que el usuario no ingrese una opción correcta se volverá a pedir que
ingrese una opción
Ejecutar la operación
Mostrar por pantalla el resultado"""

def main():
    print("Ingrese dos números:\n")
    nro1 = int(input("Número 1: "))
    nro2 = int(input("Número 2: "))
    res = ''
    while res == '':
        op = int(input("Indique una operacion:\n1. Sumar\n2. Restar\n3. Multiplicar\n"))
        if op == 1:
            res = nro1 + nro2
        elif op == 2:
            res = nro1 - nro2
        elif op == 3:
            res = nro1 * nro2
    print(res)

if __name__ == "__main__":
    main()

"""Ejercicio 3.
Pedir al usuario que ingrese un email
Verificar si el usuario ingresó una dirección de email (basta con que tenga un
"@")
Al finalizar mostrar por pantalla si es un email o no
No utilizar in
"""
def vailidar_mail(mail):
    validacion = False
    for i in range(len(mail)):
        if mail[i] == '@':
            validacion = True
    return validacion

def main():
    mail = input("Ingrese un mail: ")
    if vailidar_mail(mail):
        print(mail," es un mail valido!")
    else:
        print("No es valido ese mail!")

if __name__ == "__main__":
    main()

"""Ejercicio 4.
Definir una lista
Contar los elementos de esa lista
Al finalizar mostrar por pantalla la cantidad de elementos de la lista
No utilizar función len
"""
def main():
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    cont = 0
    for mes in meses:
        cont = cont + 1
    
    print(f"La lista contiene {cont} elementos")

if __name__ == "__main__":
    main()

"""Ejercicio 5.
Definir una lista de números
Sumar todos sus valores de esa lista
Al finalizar mostrar por pantalla el total de la suma.
No utilizar función sum
"""
def main():
    numeros = [1,3,5,7,10,16,23]
    suma = 0
    for num in numeros:
        suma = suma + num
    
    print(f"La suma total de la lista es de {suma}")

if __name__ == "__main__":
    main()

"""Ejercicio 6.
Definir una lista de números
Mostrar por pantalla el valor promedio de la lista.
No utilizar funciones sum ni len"""
def main():
    numeros = [1,3,5,7,10,16,23]
    suma = 0
    cont = 0
    for num in numeros:
        suma = suma + num
        cont = cont + 1
    
    res = suma/cont
    print(f"El promedio de la lista es de {res}")

if __name__ == "__main__":
    main()

"""Ejercicio 7.
Definir una lista de números
Encontrar el valor máximo de la lista
Imprimir el valor
No utilizar max"""

def main():
    numeros = [-50,1,3,70,5,7,10,16,23,50]
    num_max = -1000
    for num in numeros:
        if num > num_max:
            num_max = num
    
    print(f"El valor máximo de la lista es {num_max}")

if __name__ == "__main__":
    main()

"""Ejercicio 8.
Definir una lista de números
Encontrar el valor mínimo de la lista
Imprimir el valor
No utilizar min"""
def main():
    numeros = [1,3,70,5,7,10,16,-1,23,50]
    num_min = 10000000
    for num in numeros:
        if num < num_min:
            num_min = num
    
    print(f"El valor mínimo de la lista es {num_min}")

if __name__ == "__main__":
    main()