print("\n###########################################################\n")

asterik_shape_list = [5,2,5,2,2]

for number in asterik_shape_list:
    line = ""
    for i in range(number):
        line += "*"
    print(line)

print("\n###########################################################\n")


pyramid_length = 5
num_itr = (pyramid_length * 2) - 1

lines_num = 0
while lines_num < num_itr:
    lines_num += 1 
    asterik_num = 0
    if lines_num <= pyramid_length:
        asterik_num = lines_num
    else:
        asterik_num = (num_itr + 1) - lines_num
    
    line = ""
    for i in range(asterik_num):
        line += "*"
    print(line)

print("\n###########################################################\n")

line = ""
while len(line) < lines_num:
    line += "*"
    print(line)


while len(line) > 1:
    line = line[:-1]
    print(line)