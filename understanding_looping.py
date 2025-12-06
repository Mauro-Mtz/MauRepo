magicians = ['ron', 'harry', 'hermione', 'snape', 'draco']

for magician in magicians:
    print(magician)
    print(magician.upper())
    print(f"{magician.title()} ese fue un gran hechizo!")
    print("\n")
print("Gracias a todos por participar en el espectaculo de hoy!")   

"""
la 'identacion' es la forma en que python reconoce que un bloque de codigo
pertenece a una estructura de control como un ciclo for.
la 'identacion' de python es de 4 espacios.

basicamente se utilizan 4 espacios en blanco para 
obligarnos a escribir codigo ordenado y estructurado.
"""

#No olvidemos identar (donde se necesita)
#Ejemplo 
magician = ['alice', 'david', 'jorge']
for magician in magician:
    print(magician) #Solucion

#Identacion Error 
magicians = ['alice', 'david', 'jorge', 'candelario']   
for magician in magicians:
    print(magician) #Error de identacion
#print(f'great {magician}!, i cant wait to see your next trick.')
    print(f'great {magician}!, i cant wait to see your next trick.') #Solucion

# Identacion innecesaria
message = "Hello Charly"
#    print(message) #Error de identacion
print(message) #Solucion 

#logical error
magicians = ['alice', 'david', 'jorge', 'candelario'] 
for magician in magicians:
    print(magician) 
    print(f'great {magician}!, i cant wait to see your next trick.')
print("Thank you everyone, that was a great magic show!") 

#error de sintaxis
magicians = ['alice', 'david', 'jorge', 'candelario']
for magician in magicians: # SyntaxError sucede cuando falta el colon :
    print(magician)
    