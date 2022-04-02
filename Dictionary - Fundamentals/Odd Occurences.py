words = input().split()
dictionary = {}

for i in range(0, len(words), 1):
    lower = words[i].lower()
    if lower not in dictionary:
        dictionary[lower] = 0
    dictionary[lower] += 1

for (key, value) in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")
