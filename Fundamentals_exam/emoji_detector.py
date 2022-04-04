import re
string = input()
pattern = r"(\:\:|\*\*)([A-Z][a-z]{2,})\1"
is_valid = re.findall(pattern, string)
threshold = 1
summ = 0
for i in string:
    if i.isdigit():
        threshold *= int(i)
print(f"Cool threshold: {threshold}")
print(f"{len(is_valid)} emojis found in the text. The cool ones are:")
k = ""
for i in range(len(is_valid)):
    summ = 0
    for k in is_valid[i][1]:
        summ += ord(k)
    if summ >= threshold:
        print(f"{is_valid[i][0]}{is_valid[i][1]}{is_valid[i][0]}")
