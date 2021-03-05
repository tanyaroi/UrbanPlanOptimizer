#numbers_list = []
numbers_list = [1,2,3,4,5]

# bad O(n^2) example
for number in numbers_list:
    for number2 in numbers_list:
        not_max = number2 > number
        if not_max:
            break
    if not not_max:
        print(number)


# good O(n) example
output = "empty list"
if len(numbers_list):    
    local_min = numbers_list[0]
    for number in numbers_list:
        if number < local_min:
            local_min = number
    output = local_min
print(output)