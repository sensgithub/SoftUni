text = input()
litres = int(input())

fuel_type = ["Gas", "Gasoline", "Diesel"]

if text not in fuel_type:
    print("Invalid fuel!")
else:
    if litres >= 25:
        print(f"You have enough {text.lower()}.")
    elif litres < 25:
        print(f"Fill your tank with {text.lower()}!")
