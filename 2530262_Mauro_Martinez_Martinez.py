##Nombre: Mauro Martínez Martínez
##Matrícula: 2530262
## Grupo: IM 1-2

"""
PROBLEM: Fibonacci series generator

Description: Program that reads an integer n and prints
the first n terms of the Fibonacci series starting at 0 and 1.
Inputs: n (int)
Outputs: Fibonacci series values
Validations: integer, n >= 1, optional n <= 50
Test cases:
1) Normal: n = 5 -> 0 1 1 2 3
2) Border: n = 1 -> 0
3) Error: n = -3 -> Error: invalid input
"""

#CODE STARTS HERE


user_input = input("Number of terms: ")

try:
    terms_count = int(user_input)
    if terms_count < 1 or terms_count > 50:
        print("Error: invalid input")
    else:
        print("Fibonacci series:", end=" ")
        current_term = 0
        next_term = 1

        if terms_count == 1:
            print(current_term)
        else:
            print(current_term, next_term, end=" ")
            for _ in range(terms_count - 2):
                new_term = current_term + next_term
                print(new_term, end=" ")
                current_term = next_term
                next_term = new_term
except:
    print("Error: invalid input")


#CONCLUSIONES

"""
Generar la serie de Fibonacci mediante un bucle me permitió 
entender mejor cómo cada término depende del anterior y cómo 
controlar la lógica paso a paso. También pude observar que manejar
correctamente casos como n = 1 o n = 2 evita errores y hace
que el programa sea más robusto. Además, estructurar el código 
con validaciones claras ayuda a que el usuario reciba mensajes más
precisos cuando ingresa datos incorrectos. Este ejercicio también me hizo ver 
que la idea básica del algoritmo puede reutilizarse en otros programas 
que trabajen con secuencias o acumulación de valores.
"""

#REFERENCIAS

"""
1) Python docs – loops
2) Fibonacci tutorials
3) Apuntes de clase
"""