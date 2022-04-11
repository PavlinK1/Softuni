import re

pattern = r"(\:\:|\*\*)([A-Z][a-z]{2,})\1"
string = input()
check = re.findall(pattern, string)
threshold = 1

emoji_count = len(check)
emoji_coolness = 0

for every in range(len(string)):
    if string[every].isdigit():
        threshold *= int(string[every])
print(f"Cool threshold: {threshold}")

print(f"{emoji_count} emojis found in the text. The cool ones are:")
for key, value in check:
    emoji_coolness = 0
    for i in range(len(value)):
        emoji_coolness += int(ord(value[i]))
    if emoji_coolness >= threshold:
        print(f"{key}{value}{key}")


