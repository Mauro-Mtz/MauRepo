#SLICING
players = ['cr7', 'messi', 'Travis', 'chicha', 'corona']
print(players[0:3])

#slice es trabajar con un grupo especifico en una lista 
print(players[1:4]) #salida: ['messi', 'Travis', 'chicha']
print(players[:4]) #salida: ['cr7', 'messi', 'Travis', 'chicha'
print(players[2:]) 
print(players[-3:])

#Slicing en un for
players = ['axel', 'ignacio', 'travis', 'cr7', 'messi', 'Travis', 'chicha', 'corona', 'jorge']
first_three_players = players[0:4]
print("\nfirst_three_players:\n ", first_three_players)

print("\nAqui vienen los tres mejores del salon:\n ")
for player in players[0:3]:
    print(player.upper())

#copia de listas 
my_food = ['pizza', 'gorditas de jaumave', 'machacado']
#copy_of_food = my_food # manera incorrecta de copiar una lista
copy_of_food_1 = my_food[:]
copy_of_food_2 = my_food.copy
copy_of_food_3 = list(my_food)

cars = ['bwm', 'porch', 'masda', 'totoyta', 'ford']
cars[0]="bmw"
cars[1]="porshe"
cars[2]="mazda"
cars[3]="toyota"
