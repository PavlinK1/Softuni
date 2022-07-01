word = input()
dictionary = {}

for i in range(0, len(word)):
    if word[i] != " ":
        if word[i] not in dictionary:
            dictionary[word[i]] = 1
        else:
            dictionary[word[i]] += 1
for key, value in dictionary.items():
    print(f"{key} -> {value}")
