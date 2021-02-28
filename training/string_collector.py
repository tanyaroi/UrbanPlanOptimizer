inputs_list = []

while True:
    user_input = input("> ").lower()

    if user_input == "$quit":
        for item in inputs_list:
            print(item)
        break
    
    elif user_input == "$sum":
        total = 0
        for item in inputs_list:
            total += item
        print(total)
    
    elif user_input == "$mult":
        total = 1
        for item in inputs_list:
            total *= item
        print(total)

    elif user_input == "$rlast":
        inputs_list = inputs_list[0:-1]
        for item in inputs_list:
            print(item)
        
    elif user_input.isnumeric():
        inputs_list.append(int(user_input))
    
    else:
        print("please use allowed commands")