import re
names = input().split(", ")
pattern = r"[A-Za-z]{1,}"
chars = input()
words = re.findall(pattern, chars)
dictionary = {}
n = 3
while chars != "end of race":
    name = "".join(words)
    sum_digits = 0
    if name in names:
        for i in range(len(chars)):
            if chars[i].isdigit():
                sum_digits += int(chars[i])
        if name not in dictionary:
            dictionary[name] = sum_digits
        else:
            dictionary[name] += sum_digits
    chars = input()
    words = re.findall(pattern, chars)
for i in range(n):
    biggest = max(dictionary, key=dictionary.get)
    if i == 0:
        print(f"1st place: {biggest}")
    elif i == 1:
        print(f"2nd place: {biggest}")
    elif i == 2:
        print(f"3rd place: {biggest}")
    dictionary.pop(biggest)