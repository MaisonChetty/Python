quit_game=False
car_started=False
while not quit_game:
    command = input("Enter a command: ").lower()

    if command == "start" and car_started == False:
        car_started=True
        print("Car started...")
    elif command == "start" and car_started == True:
        print("Car is already started!")
    elif command == "stop" and car_started == True:
        car_started=False
        print("Car stopped.")
    elif command == "stop" and car_started == False:
        print("Car is already stopped!")
    elif command == "quit":
        quit_game = True
        break
    elif command == "help":
        print("""start - to start the car
stop - to stop the car
quit - to exit the game
              """)
    else:
        print("I don't understand that command. if you need help type 'help'")