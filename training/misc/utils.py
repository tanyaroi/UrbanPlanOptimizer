def find_max(numbers):
    try:
        max = numbers[0]

        for number in numbers:
            if number > max:
                max = number

    except IndexError as index_error:
        print(index_error)
    
    return max


# try:
#     max = numbers[0]
#     no_except = True

# except IndexError as index_error:
#     print(index_error)
#     no_except = False

# if no_except:
#     for number in numbers:
#         if number > max:
#             max = number
#     print(max)
