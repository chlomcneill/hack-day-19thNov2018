def length_of_last_word(string):
    if len(string.replace(" ", "")) == 0:
        return 0
    else:
        string = string.split()
        length = len(string)
        return len(string[length-1])

print(length_of_last_word("Hello world"))