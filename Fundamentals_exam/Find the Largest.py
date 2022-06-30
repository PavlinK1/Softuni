# number = int(input())
#
# for digit in range(number):
#     print(digit)
#     print(number)

number = int(input())
n = str(number)

m = sorted(n, reverse=True)


for d,digit in enumerate(m):
    print(digit, end="")