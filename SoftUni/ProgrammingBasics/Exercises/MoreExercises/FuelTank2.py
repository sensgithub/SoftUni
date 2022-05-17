fuel_type = input()
liters = float(input())
club_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

total_gasoline = 0
total_diesel = 0
total_gas = 0

if club_card == "Yes":
    gasoline_price = gasoline_price - 0.18
    diesel_price = diesel_price - 0.12
    gas_price = gas_price - 0.08

if 20 <= liters <= 25:
    total_gasoline = liters * gasoline_price * 0.92
    total_diesel = liters * diesel_price * 0.92
    total_gas = liters * gas_price * 0.92

if liters > 25:
    total_gasoline = liters * gasoline_price * 0.90
    total_diesel = liters * diesel_price * 0.90
    total_gas = liters * gas_price * 0.90

if liters < 20:
    total_gasoline = liters * gasoline_price
    total_diesel = liters * diesel_price
    total_gas = liters * gas_price

if fuel_type == "Gasoline":
    print(f"{total_gasoline:.2f} lv.")

if fuel_type == "Diesel":
    print(f"{total_diesel:.2f} lv.")

if fuel_type == "Gas":
    print(f"{total_gas:.2f} lv.")
