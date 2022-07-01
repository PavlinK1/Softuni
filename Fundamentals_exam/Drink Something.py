kids_drink = "drink toddy"
teens_drink = "drink coke"
young_adults_drink = "drink beer"
adults_drink = "drink whisky"
age = int(input())

if age <= 14:
    print(kids_drink)
elif age <= 18:
    print(teens_drink)
elif age <= 21:
    print(young_adults_drink)
elif age > 21:
    print(adults_drink)