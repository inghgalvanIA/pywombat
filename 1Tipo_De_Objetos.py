#Imprime en consola el tipo de objeto de cada uno de los elemento que contiene la lista.

lista = ['Hola Mundo', 234, [4, 3, 2, 1], ('H', 'o', 'l', 'a'), 25.02, {1: 'M', 2: 'u', 3: 'n', 4: 'd', 5: 'o'}]

for i in lista:
    print(f"el valor {i} es de tipo {type(i)}")