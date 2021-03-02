def emoji_mapper(user_input):
    output = ""
    emoji_dict = {
        ":)" : "😊",
        ":(" : "☹️",
        ":*" : "😙",
        ";)" : "😉",
        ":|" : "😐"
    }

    words = user_input.split(" ")

    for word in words:
        output += emoji_dict.get(word, word) + " "
    
    return output

#print(emoji_mapper(input("> ")))
print(emoji_mapper("Puff :("))
print(emoji_mapper("Jigly :)"))
print(emoji_mapper("JiglyPuff :|"))