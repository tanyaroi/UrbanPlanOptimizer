while True:
    user_input = input("> ").lower()

    if user_input == "quit":
        break
        
    if user_input == "help":
        print('''start - starts the car
stop - stops the car
quit - exit game''')

    elif user_input == "start":
        print("car started, ready to go!")
    
    elif user_input == "stop":
        print("car stopped")
    
    else:
        print("sorry, I don't understand that")