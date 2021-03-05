# prices = [10, 20, 30]
# sum = 0

# for price in prices:
#     sum = sum + price
# print(sum)


numbers = [2,2,2,2,6]
line = ""

for number in numbers:
    for i in range(number):
        line = line + "x"
    print(line)
    line = ""


for i in range(1,100):
    if i % 3 == 0:
        total += i
    elif i % 5 == 0:
        total += i
print(total)


for i in range(1,100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)