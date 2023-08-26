
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