digits_words_dict = {
    "0" : "Zero",
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine"
}

user_input = input("Phone: ")
line = ""

for digit in user_input:
    line += digits_words_dict[digit] + " "
print(line)


digits_words_list = [
  "Zero",
  "One",
  "Two",
  "Three",
  "four",
  "Five",
  "Six",
  "Seven",
  "Eight",
  "Nine"
]

line = ""
for digit in user_input:
    line += digits_words_list[int(digit)] + " "
print(line)

user_input = input("> ")
output = ""
emoji_dict = {
    ":)" : "😊",
    ":(" : "☹️",
    ":*" : "😙",
    ";)" : "😉"
}

words = user_input.split(" ")

for word in words:
    output += emoji_dict.get(word, word) + " "
print(output)
