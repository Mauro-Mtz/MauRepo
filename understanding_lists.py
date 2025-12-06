#LISTAS

#una lista es una coleccion ordenada y mutable de elementos
#se pueden crear listas utilizando corchetes [] y separando los elementos con comas ,
fruits = ['Manzana', 'banana', 'cereza']
print(fruits)   #salida: ['Manzana', 'banana', 'cereza']

#acceso a los elementos de una lista
print(fruits[0].upper())  #salida: MANZANA
print(fruits[2].title())  #salida: Cereza
print(fruits[1].lower())  #salida: banana   

#print(fruits[3])  #IndexError: list index out of range 

# Acceder a los elementos de una lista utilizando indices negativos
print(fruits[-1])  #salida: cereza
print(fruits[-2])  #salida: banana      
print(fruits[-3])  #salida: Manzana 

"""
una lista es mutable por que podemos cambiar sus elementos despues de haberla creado
"""

message = f'mi fruta favorita es {fruits[0].title()}.'  
print(message) #salida: mi fruta favorita es Manzana.

print("\nAgregar elementos a una lista: metodo append()\n")
"""
agregar elementos de una lista
-append(): agrega un elemento al final de la lista
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  #salida: ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)  #salida: ['honda', 'yamaha', 'suzuki', 'ducati']

"""
insert(): inserta un elemento en una posicion especifica de la lista
"""

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  #salida: ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)  #salida: ['ducati', 'honda', 'yamaha', 'suzuki']   
motorcycles = ['honda', 'yamaha', 'suzuki'] 
motorcycles.insert(-2, 'ducati') 
print(motorcycles)  #salida: ['honda', 'yamaha', 'ducati', 'suzuki']

"""
    Eliminar elementos de una lista
    -del: elimina un elemento de la lista en una posicion especifica 
    la declaracion del index elimina el elemento en la posicion especificada
"""

print("\nEliminar elementos de una lista: del\n")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  #salida: ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)  #salida: ['yamaha', 'suzuki']   

"""
eliminar el elemento de una lista 
- pop(): Elimina y devuelve el ultimo elemento de la lista
el metodo pop()
"""

print("\n eliminar elemtos de una lista: metodo pop")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  #salida: ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)  #salida: ['honda', 'yamaha']
print(f'la ultima motocicleta eliminada es {popped_motorcycle}.')

"""
eliminar un elemento en una posicion especifica de la lista utilizando pop(index)
pop(index): elimina y devuelve el elemento en la posicion especificada  
el metodo pop(index) toma un indice como argumento y elimina el elemento en esa posicion
"""
print("\nEliminar elementos de una lista: metodo pop(index)\n")
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)  #salida: ['honda', 'yamaha', 'suzuki']
first_motorcycle = motorcycles.pop(0)   
print(motorcycles)  #salida: ['yamaha', 'suzuki']
print(f'la primera motocicleta eliminada es {first_motorcycle}.')
""" 
eliminar elementos de una lista 
remove(): elimina la primera aparicion de un valor especifico
el metodo remove(value) toma un valor como argumento y elimina la primera aparicion de ese valor en la lista
"""
print("\nEliminar elementos de una lista: metodo remove\n")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 'yamaha']
print(motorcycles)  #salida: ['honda', 'yamaha', 'suzuki', 'ducati', 'yamaha']
motorcycles.remove('yamaha')
print(motorcycles)  #salida: ['honda', 'suzuki', 'ducati', 'yamaha']


#Ejemplo practico del metodo remove()
names = ['ana', 'agripino', 'pedro', 'maria', 'pancrasio', 'juan']
print(names)  #salida: ['ana', 'agripino', 'pedro', 'maria', 'pancrasio', 'juan']
deleted_name = input("\n \n ingresa el nombre que deseas eliminar: ")
names.remove(deleted_name.strip().lower())
print(names)

"""
ordenar listas 
metodo de listas: sort()
ordenamiento permanente de una lista
el metodo sort() ordena los elementos de una lista en orden alfabetico o numerico
"""
#ordenamiento ascendente
print("\nOrdenar listas: metodo sort()\n")
cars = ["bmw", "audi", "ford", "kia"]
print(cars)  #salida: ['bmw', 'audi', 'ford', 'kia']
cars.sort(reverse=True) 
print(cars)  #salida: ['audi', 'bmw', 'ford', 'kia']    

""" 
reverse(): invierte el orden de los elementos en la lista
el metodo reverse() invierte el orden de los elementos en la lista
"""
print("\nOrdenar listas: metodo reverse()\n")
motorcycles2 = ['mortalica', 'honda', 'ducati']
print(motorcycles2)  #salida: ['mortalica', 'honda', 'ducati']
motorcycles2.reverse()
print(motorcycles2)  #salida: ['ducati', 'honda', 'mortalica']

"""
 cantidad de elementos en una lista metodo built-in len()
len(): devuelve el numero de elementos en una lista 
"""

cars2 = ['ford', 'chevrolet', 'nissan']
print("\nCantidad de elementos en una lista: metodo len()\n")
print(len(cars2))  #salida: 3   

"""
metodo built-in sorted()
sorted(): ordena la lista temporalmente sin modificar la lista original

"""

favorite_students = ['jorge', 'jose', 'carlos', 'emiliano']     
print(favorite_students)  #salida: ['jorge', 'jose', 'carlos', 'emiliano']

print(sorted(favorite_students))  #salida: ['carlos', 'emiliano', 'jorge', 'jose']

print(f"lista ordenada temporalmente: {sorted(favorite_students)}")

print(f"lista original: {favorite_students}")

#tuplas 
#listas