# Exercise : Pgm to find the most repeated character in the given set

sentence = "This is a common interview question"
characters = sentence.replace(' ', '')
char_dictionary = {}
for item in characters:
    if item in char_dictionary:
        char_dictionary[item] += 1
    else:
        char_dictionary[item] = 1

frequent_char = sorted(char_dictionary.items(), key=lambda keyvalue:keyvalue[1], reverse=True)  # this method returns all key-value pairs as tuples
print(frequent_char[0])



