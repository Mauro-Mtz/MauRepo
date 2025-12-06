"""
las tuplas son valores inmutables almacenados de una estrcutura de datos
se puede hacer una tupla utiizando ()
"""


#Rectangulo (largo, ancho)

rectangle_dimension = (200, 50) #tupla
print(rectangle_dimension)
print(f" largo {rectangle_dimension[0]} mm")
print(f" amcho {rectangle_dimension[1]} mm")

# vamos a intentar modificar una tupla
# rectangle_dimension[0] = 250 # Error de tipo TypeError
# rectangle_dimension[1] = 100 # Error de tipo TypeError

for dimension in rectangle_dimension:
    print(dimension)

"""
    No podemos modificar una tupla, ni tampoco agregar/eliminar
    elementos. lo que si podemos hacer es cambiar la asignacion a 
    una variable que almacena una tupla
"""

rectangle_dimension = (300, 150) #tupla

