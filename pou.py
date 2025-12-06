from colorama import init, Fore, Style
import time

init(autoreset=True)

alien = {
    "color": "green",
    "points": 5,
    "x_position": 0,
    "y_position": 25
}

def show_alien():
    print(Fore.CYAN + "\n=== ALIEN STATUS ===")
    print(Fore.GREEN + f"Color: {alien['color']}")
    print(Fore.YELLOW + f"Points: {alien['points']}")
    print(Fore.MAGENTA + f"X Position: {alien['x_position']}")
    print(Fore.MAGENTA + f"Y Position: {alien['y_position']}")
    print(Fore.CYAN + "====================\n")

def move_alien():
    direction = input(Fore.BLUE + "Move alien (left / right / up / down): ").lower()
    
    if direction == "right":
        alien["x_position"] += 5
    elif direction == "left":
        alien["x_position"] -= 5
    elif direction == "up":
        alien["y_position"] += 5
    elif direction == "down":
        alien["y_position"] -= 5
    else:
        print(Fore.RED + "Invalid direction!")

def change_color():
    new_color = input(Fore.BLUE + "Choose new color (green / yellow / red / purple): ").lower()
    
    if new_color in ["green", "yellow", "red", "purple"]:
        alien["color"] = new_color
    else:
        print(Fore.RED + "Invalid color!")

def battle():
    print(Fore.RED + "\nAlien encountered an enemy!")
    choice = input(Fore.YELLOW + "Fight or Run? ").lower()

    if choice == "fight":
        alien["points"] += 10
        print(Fore.GREEN + "You won the battle! +10 points")
    else:
        alien["points"] -= 5
        print(Fore.RED + "You ran away... -5 points")

def main():
    while True:
        print(Fore.CYAN + "\nWhat do you want to do?")
        print(Fore.WHITE + "1 - Show Alien")
        print(Fore.WHITE + "2 - Move Alien")
        print(Fore.WHITE + "3 - Change Alien Color")
        print(Fore.WHITE + "4 - Battle")
        print(Fore.WHITE + "5 - Exit")

        option = input(Fore.YELLOW + "\nChoose an option: ")

        if option == "1":
            show_alien()

        elif option == "2":
            move_alien()

        elif option == "3":
            change_color()

        elif option == "4":
            battle()

        elif option == "5":
            print(Fore.CYAN + "Goodbye, Commander 👽")
            break

        else:
            print(Fore.RED + "Invalid option!")


main()
