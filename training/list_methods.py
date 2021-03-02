numbers = [5, 2, 7, 20, 7, 8, 5]
numbers_set = []

for number in numbers:
    if number not in numbers_set:
        numbers_set.append(number)
print(numbers_set)


for number in numbers:
    while numbers.count(number) > 1:
        numbers.remove(number)
print(numbers)

print(set(numbers))