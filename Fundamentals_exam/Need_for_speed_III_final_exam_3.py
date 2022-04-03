n = int(input())
dictionary = {}
fuell = 0
for i in range(n):
    car, mileage, fuel = input().split("|")
    dictionary[car] = {"mileage": int(mileage), "fuel": int(fuel)}


stop_command = input()
command = stop_command.split(" : ")
while stop_command != "Stop":
    if command[0] == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if dictionary[car]["fuel"] < fuel:
            print(f"Not enough fuel to make that ride")
        elif dictionary[car]["fuel"] >= fuel:
            dictionary[car]["mileage"] += distance
            dictionary[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if dictionary[car]["mileage"] >= 100000:
            dictionary.pop(car)
            print(f"Time to sell the {car}!")
    elif command[0] == "Refuel":
        car = command[1]
        fuel = int(command[2])
        if dictionary[car]["fuel"] == 75:
            print(f"{car} refueled with {fuel} liters")
        elif dictionary[car]["fuel"] < 75:
            old = dictionary[car]["fuel"]
            dictionary[car]["fuel"] += fuel
            if dictionary[car]["fuel"] > 75:
                fuel = 0
                while dictionary[car]["fuel"] > 75:
                    fuel = 75 - old
                    dictionary[car]["fuel"] -= 1
            print(f"{car} refueled with {fuel} liters")
    elif command[0] == "Revert":
        car = command[1]
        kilometers = int(command[2])
        dictionary[car]["mileage"] -= kilometers
        if dictionary[car]["mileage"] > 10000:
            print(f"{car} mileage decreased by {kilometers} kilometers")
        elif dictionary[car]["mileage"] < 10000:
            dictionary[car]["mileage"] = 10000
    stop_command = input()
    command = stop_command.split(" : ")
for key, value in dictionary.items():
    print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")
