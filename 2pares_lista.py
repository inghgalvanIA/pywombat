"""
Desarrolla un programa en Python que nos permita conocer todos los números pares dentro de una lista.

El usuario podrá crear una lista de longitud n.
El usuario podrá definir la longitud y cada uno de los elementos dentro de la lista.
Todo los elementos dentro de la lista serán números enteros.
El programa deberá mostrar en consola todos los números pares que comprende la lista.
En caso no existan números pares el programa no deberá imprimir nada.

Ejemplos.

$ python main.py
Longitud de la lista: 3

Ingresa un elemento: 1
Ingresa un elemento: 2
Ingresa un elemento: 3

2
$ python main.py
Longitud de la lista: 6

Ingresa un elemento: 11
Ingresa un elemento: 20
Ingresa un elemento: 30
Ingresa un elemento: 10
Ingresa un elemento: 20
Ingresa un elemento: 20

20
30
10
20
20
"""

longitud = int(input("Ingresa la longitud de la lista"))
lista= []

print(longitud)

contador = 1

while contador <= longitud:
    var = int(input("Ingrese un elemento: "))
    lista.append(var)
    contador = contador + 1

for i in lista:
    if i % 2 == 0:
        print(i)
    else:
        pass

"""
length = input('Longitud de la lista: ')

new_list = [  int(input('ingresa un valor: ')) for _ in range(int(length)) ]

[print(val) for val in new_list if val % 2 == 0]

"""
