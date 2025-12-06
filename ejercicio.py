age = int (input("Dime ¿Cual es tu edad? "))

if age <= 4:
    print("la entrada es gratuita")
elif age <= 18 and age > 4:
    print("la entrada cuesta $200")
elif age > 18 and age <= 99:
    print("entonces la entrada cuesta $400")
elif age > 100:
    print("Que haces aqui wey, vete a dormir ya estas viejo")
else: 
    print("edad no valida")