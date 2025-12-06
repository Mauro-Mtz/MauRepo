cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car)


#El condicional es el corazon de un if
#Condicional
car = "bmw"
print(car=='bmw') #True

#Condicional False 
car = "Audi"
print(car == 'audi') #False

#posible solucion 
car = "Audi"
print(car.lower()=='audi') #True

#operador relacional != para determinar desigualdad
requested_topping = "mushroom"
if requested_topping != "anchovies": #True
    print("Hold the archovies")

# Comparaciones numericas 
age = 18 #Entero
print(age==18) #True

answer = 17
if answer != 42: #True
    print("Esa no es la respuesta correcta. Intenta otra vez")

age = 17 
print(age < 21) #True
print(age <= 21) #True
print(age > 21) #false 
print(age >= 21) #false 

# Multiples condiciones
age_0 = 22
age_1 = 18
#Operacion "and"
print( age_0 >= 21 and age_1 >= 21) #False 
print( age_0 >= 21 and age_1 >= 18) #True

#operacion "or"
print( age_0 >= 21 or age_1 >= 21) #True
print( age_0 >= 23 or age_1 >= 21) #false

"""
    para preguntarnos si un valor especifico 
    esta en una lista, podemos utilizar el 
    siguente comparador:

    value in list
"""
motorcycles = ['mprtalica', 'honda', 'vento', 'yamaha']
moto_Charly_want = "italica"
print(moto_Charly_want in motorcycles) #False 
print("honda" in motorcycles) #True


"""
    para preguntarnos si un valor especifico 
    NO esta en una lista, podemos utilizar el 
    siguente comparador:

    value not in list
"""

banned_student = ['jorge', 'carlos', 'moyra', 'gus', 'hots']
user = "mauro"
print(user not in banned_student) # True 
print("jorge" not in banned_student) #False 

# Variable del tipo b0oleano
game_active = True
can_edit = False

"""
    if statement

    sintaxis:

    if condition:
        do something

    if condition:
        do something
    else: 
        do something
"""
