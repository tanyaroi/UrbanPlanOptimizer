# 1. whiles and fors < 30min
#     a. user gets interactive console ("> ")
#     b. user can enter numbers
#     c. if user enters a number which already exists, notify the user and remove the number from the list
#     d. user can also enter special commands that start with '$quit', '$sum', '$mult', '$avg' '$rlast', '$rfirst'

numbers_list = []

while True:
    user_input = input("> ")

    if user_input == "$quit":
        for item in numbers_list:
            print(item)
        break

    elif user_input == "$sum":
        total = 0
        for number in numbers_list:
            total += number
        print(total)

    elif user_input == "$mult":
        total = 1
        for number in numbers_list:
            total *= number
        print(total)

    elif user_input == "$avg":
        total = 0
        for number in numbers_list:
            total += number
        total //= len(numbers_list)
        print(total)
    
    elif user_input == "$rlast":
        numbers_list = numbers_list[0:-1]
        for number in numbers_list:
            print(number)
    
    elif user_input == "$rfirst":
        numbers_list = numbers_list[1:]
        for number in numbers_list:
            print(number)
    
    elif user_input.isnumeric():
        
        user_input = int(user_input)

        if user_input in numbers_list:
            numbers_list.remove(user_input)
            print("number removed from list")
        else:
            numbers_list.append(user_input)    
    
    else:
       print("I don't understand")         
    