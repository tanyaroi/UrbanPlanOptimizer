is_started = False

while True:
        user_input = input("> ").lower()

    if user_input == "quit":
        if is_started:
            print("Please stop the car first")
        else:
            break

    elif user_input == "help":
        print("start | stop | quit | help")

    elif user_input == "start":
        if is_started:
            print("already started")
        else:
            print("starting...")
            is_started = True

    elif user_input == "stop":
        if not is_started:
            print("already stopped")
        else:
            print("stopped")
            is_started = False

    else:
        print("I don't understand")