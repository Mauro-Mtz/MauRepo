""" 
    vamos a realizar un programa que pregunte al usuario su edad
    y corroborar que es mayor de edad y muestre un mensaje diferente segun el rango 
    de edad en el que se encuentre:
"""

age = 0
try:
    age = int(input("Por favor, introduce tu edad: "))
except:
    age = -1

    
    
if age >= 100: 
    print("Tienes mas de un siglo de vida.")
elif age >=  18 and age <= 100:
    print("Eres mayor de edad")
elif age < 18 and age >= 0:
    print("Eres menor de edad.")
elif age < 0:
    print("Tuviste un error al ingresar un caracter no valido.")

print("Hola Mauro")

"""
    hacer un programa que pregunte la edad de una persona y responda lo siguiente:
       - si la edad es menor e igual a 4, la entrada es gratuita
       - si la edad es menor e igual a 18, pero mayor que 4, la entrada cuesta $200
       - si la edad es mayor que 18, entonces la entrada cuesta $400
"""

# Multiple if 
