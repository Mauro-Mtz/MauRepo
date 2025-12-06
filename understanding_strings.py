""" 
    un string es de manera sencilla una secuencia de caracteres.
    en python los strings se definen utilizando comillas simples (' '),
    comillas dobles (" ") 

     "esto es un string"
     'esto tambien es un string'

     'le dije a un amigo, "!Python es mi lenguaje favorito!"'
     "el lenguaje de 'Python' lleva el nombre por Monty Python,
     no por la serpiente."

"""

name = "clase de programacion"
print(name)
print(name.title())
print(name.upper())
print(name.lower())

"""

un  metodo es una accion que python puede realizar en un fragmento de datos
sobre una variable.

El punto . despues dr una variable seguida del metodo title() dice que se tiene 
que ejecutar el metodo title() de la variable name.

todos los metodos van seguidos de parentesis (). por que en ocaciones necesitan 
informacion adicional para funcionar. lo cual iria dentro de los parentesis.
en esta ocasion el metodo .title() no necesita informacion adicional para ejecutarse.

"""

# concatenacion de strings
print("concatenacion de strings")
first_name = "mauro"
last_name = "martinez"
full_name = first_name + " " + last_name
print(full_name)

print("Hola, " + full_name.title() + "!")

message = "una fortaleza de python es su comunidad de usuarios."
print(message)

message = "una fortaleza de 'python' es su comunidad de usuarios."
print(message)

"""
sintax error se produce cuando el codigo no sigue las reglas del lenguaje.
"""

famous_person = "Biggie cheese"
quote = "python is love, python is life" 

#concatenacion convencional
message = famous_person + " una vez dijo " + quote
print(message)

#concatenacion con f strings
message_f_string = f"{famous_person} una vez dijo {quote}"
print(message_f_string)


#actividad

"""
1) elije un personaje famoso e igualalo a una variable de tipo string
2) elige una frase famosa que haya dicho esta persona e igualalo a una
 variable de tipo string
3) genera un mensaje con las dos variables utilizando f strings
4) imprime el mensaje
"""

very_famous_person = "socrates" 
message_of_the_person = "Solo se que no se nada"

that_message = f"{very_famous_person} una vez dijo {message_of_the_person}"
print(that_message)


#whitespaces 
"""
whitespace se refiere a cualquier caracter que no se imprime, como 
espacios, tabulaciones y saltos de linea.   
"""
print("python")
print("\tpython")
print("\t\tpython")

# ejemplo de salto de linea 
print("lenguajes: \n Python \n C \n javaScript")

# eliminar whitespaces en blanco
programming_language = " python "
print(programming_language)
print(programming_language.lstrip())  # elimina espacios a la izquierda
print(programming_language.rstrip())  # elimina espacios a la derecha
print(programming_language.strip())   # elimina espacios a ambos lados