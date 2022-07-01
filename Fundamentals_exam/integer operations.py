import math

first_number = int(input())
second_number = int(input())
third_number = int(input())
fourth_number = int(input())

add = first_number + second_number
divide = add / third_number
multiply =math.floor(divide) * fourth_number

print(math.floor(multiply))
