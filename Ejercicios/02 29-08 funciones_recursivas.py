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
if __name__ == "__main__":
    main()


