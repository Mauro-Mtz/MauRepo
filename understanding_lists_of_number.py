"""
    las listas tamien pueden almacenar numeros y de hecho son ideales para almacenarlos
    python tiene muchas funciones integradas que facilitan el trabajo con listas de numeros

    por ejemplo, funcion range() genera una secuencia de numeros enteros
"""

# la funcion range() genera una lista de numeros enteros
# en un rango especificado
#por ejemplo, para generar una lista de numeros del 0 al 9:
numeros = list(range(10))
print(numeros)  # salida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(type(numeros))  # salida: <class 'list'>

print("\nFuncion range con diferentes parametros:\n")
# podemos realizar lo mismo con un for loop
for num in range(10):
    print(num)  
    # print(type(num))  # salida: <class 'int'>

print("\ngenerando numeros en un rango especifico:\n")
for num in range(1, 5):  # genera numeros del 1 al 4
    print(num)
    # print(type(num))  # salida: <class 'int'>
number_list_1_to_4 = list(range(1, 5))
print(number_list_1_to_4)  # salida: [1, 2, 3, 4]

print("\nNumeros impares:\n")
for num in range(1, 10, 2):  # genera numeros impares del 1 al 9
    print(num)

    # print(type(num))  # salida: <class 'int'>
number_list_odd = list(range(1, 10, 2))

print("\nNumeros pares:\n")
for num in range(2, 10, 2):  # genera numeros pares del 2 al 8
    print(num)
    # print(type(num))  # salida: <class 'int'>
number_list_even = list(range(2, 10, 2))
print(number_list_even)  # salida: [2, 4, 6, 8]


# podemos crear cualquier tipo de listas con numero
# utilizando range() y list()

print("\nLista de numeros del 1 al 10:\n")
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)  # salida: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#metodos built-in para listas de numeros
print("\nFunciones built-in para listas de numeros:\n")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"Lista de digitos: {digits}")
print("valor minimo:", min(digits))  # salida: 0
print("valor maximo:", max(digits))  # salida: 9
print("suma de todos los digitos:", sum(digits))  # salida: 45
print("longitud de la lista:", len(digits))  # salida: 10
print("promedio de los digitos:", sum(digits) / len(digits))  # salida: 4.5


#list comprenhensions
""" 
    una list comprenhension combina el for loop y
    la creacion de nuevos elemntos en una sola linea de codigo 
    y tambien, automaticamente agrega el nuevo elemento a la lista es decir
    sin utilizar el append
"""
print("\nlist_comprenhensions:\n")
squares=[num**2 for num in (range(11))]
print(squares)

#numeros pares con el range
even_number_0_100 = list(range(0,101,2))
print(even_number_0_100)

#numeros pares utilizando list comprenhensions
even_list_com = [value for value in range(0,101)if value%2 > 0]
print(even_list_com)
