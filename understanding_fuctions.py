"""
    Fuctions

    Las funciones son bloques de codigo diseñados 
    para realizar una tarea especifica. 

    Cuando queremos realizar la tarea que se ha definido 
    en una funcion, tenemos que llamar el nombre de
    la funcion responsable de esto.

    Definicion de una funcion (Syntax)

    def name_of_function(parameters):
        actions

"""
def greeting_Mauro():
    print("Hola Mauro, que gusto verte!!!")

for i in  range(10):
    greeting_Mauro()

#Parametro
def greet(user_name, msj):
    print(f"Hola {user_name}, {msj}!!!")

#Argumentos 
#greeting_Mauro()
#greet("Joan", "Se te pegaron las cobijas")

""" 
vamos a realizar un programa que genere 
el nombre completo de una persona.
vamos a pasarle primer nombre, el segundo 
y el apellido 

la funcion debe generar el nombre completo
y regresarlo
"""

def create_full_name(first_name, last_name, middle_name=""):
    """
        Docstrings - Jorge This fuction creates the fullname 
        of a person give its three names.
    """
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

User_first_name = input("Escribe tu primer nombre: ").strip().lower()
User_middle_name = input("Escribe tu segundo nombre: ").strip().lower()
User_last_name = input("Escribe tu apellido: ").strip().lower()

#Argumentos Posicionales -> Positional Arguments
print(create_full_name(
    User_first_name,
    User_last_name, 
    User_middle_name))

#Argumentos Posicionales -> Positional Arguments
full_name = create_full_name(
    User_first_name,
    User_middle_name,
    User_last_name
)
print(full_name)

#Argumentos Clave -> Keyboard Arguments 
full_name_key = create_full_name(
    last_name=User_last_name,
    first_name=User_first_name,
    middle_name=User_middle_name
)
print(full_name_key)


## Parametros opcionales 
profe_falso = create_full_name(User_first_name, User_last_name)
print(profe_falso)



