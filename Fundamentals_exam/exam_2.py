import re

pattern = r"(?P<sign>U\$)(?P<username>[A-Z][a-z][a-z]{1,})\1(?P<sign_2>P\@\$)(?P<pass>[A-Za-z][A-Za-z][A-Za-z][A-Za-z][A-Za-z]{1,}\d+)\3"
tries = int(input())
count = 0
for i in range(tries):
    string = input()
    check = re.findall(pattern, string)
    if check:
        count += 1
        print("Registration was successful")
        print(f"Username: {check[0][1]}, Password: {check[0][3]}")
    else:
        print("Invalid username or password")
print(f"Successful registrations: {count}")

