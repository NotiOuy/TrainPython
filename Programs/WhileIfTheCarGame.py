
print("""
Welcome to Car Game.
To find out what commands are available to you, enter 'menu'
""")

command = ""
started = False

while True:
    command = input("> ").lower()

    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")

    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car is stopped!")

    elif command == "menu":
        print("""
start - start the car
stop - to stop the car
quit - to quit the Car Game
""")

    elif command == "quit":
        print("Game is closed.")
        break

    else:
        print("Sorry, I don't have this command. \nPlease check menu!")
