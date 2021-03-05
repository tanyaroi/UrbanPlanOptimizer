# predefined strings
help_str = '''start - to start the car
stop - to stop the car
quit - to exit'''

start_str = "car started...ready to go!"

stop_str = "car stopped"

default_str = "I don't understand that.../"

chosen_str = ""

user_input = ""

is_started = False

# interactive user prompt
while user_input != "quit":
    user_input = input(">")

    if user_input == "help":
        chosen_str = help_str
    
    elif user_input == "start":       
        if is_started:
            chosen_str = "car already started"
        else:
            chosen_str = start_str
            is_started = True
        
    elif user_input == "stop":
        if not is_started:
            chosen_str = "car already stopped"
        else:
            chosen_str = stop_str
            is_started = False
      
        
    else:
        chosen_str = default_str
        
    print(chosen_str)        