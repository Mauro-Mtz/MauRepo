# numbers

"""
   age = 33

   los podemos sumar (+), restar (-), multiplicar (*), dividir (/)

   potencias (**2, **3, )

   modulo (Dividiendo&Divisor) 
"""

number_1 = 39
number_2 = 13

suma = number_1 + number_2
difference = number_1 - number_2
multiplication = number_1 * number_2
division = number_1 / number_2
modulo = number_1 % number_2
power = number_1 ** 2

print("suma:", suma)
print("difference:", difference)        
print("multiplication:", multiplication)
print("division:", division)
print("modulo:", modulo)
print("power:", power)

print("la suma es del tipo ", type(suma))
print("la diferencia es del tipo ", type(difference))
print("la multiplicacion es del tipo ", type(multiplication))
print("la division es del tipo ", type(division))
print("el modulo es del tipo ", type(modulo))
print("la potencia es del tipo ", type(power))

#floats 
"""
los floats = reales 

son numeros con decimales
van desde -infty hasta +infty

ejemplo:

#tipado dinamico 
age = 33.5

los podemos sumar (+), restar (-), multiplicar (*), dividir (/)


"""

print(0.1 + 0.2)  
print(0.2-0.2)
print(2.5 * 2.0)

### imprimir la edad de alguien

age = 33 
message_f = f"Charly tiene {age} años"  
print(message_f)
