# Simple example of a dictionary in Python
alien_0 = {'color': 'green', 'points': 5}

#The simpliest dictionary
alien_1 = {'color': 'green'}

# accessing values in a dictionary
print(alien_1['color'])
print(alien_0['points'])

# empty dictionary
alien_2 = {}

# modifying values in a dictionary
alien_2 = {'color': 'green'}
alien_2['color'] = 'yellow'

#adding new key-value pairs
alien_2['x_position'] = 0
alien_2['y_position'] = 25
print(alien_2)



## Dictionary to store similar objects
favorite_languages = {
    'jen': 'python ',
    'sarah': 'c', 
    'edward': 'ruby',
    'phil': 'python',
}


#print(f"sarah's favorite language is {favorite_languages['sarah']}")


# looping through all key-value pairs in a dictionary
for key, value in favorite_languages.items():
    print(f"{key.title()}'s favorite \
language is {value.title()}")

# looping through all keys in a dictionary and values separately
for key in favorite_languages.keys():
    print(key)

# Looping through all values in a dictionary
for value in favorite_languages.values():
    print(value)

## nesting dictionaries

# listas de diccionarios 
# listas en diccionarios
# diccionarios en diccionarios 