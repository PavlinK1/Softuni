import math
num_p = int(input())
cap_p = int(input())

courses = math.floor(num_p / cap_p)
add_courses = num_p % cap_p

if add_courses > 0:
    courses += 1

print(courses)