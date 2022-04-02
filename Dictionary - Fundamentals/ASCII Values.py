characters = input().split(", ")
dictionary = {}

for word in characters:
    dictionary[word] = ord(word)
print(dictionary)