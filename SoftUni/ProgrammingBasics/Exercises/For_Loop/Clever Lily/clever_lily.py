age = int(input())
price_wash_machine = float(input())
toy_price = int(input())

# 1 -> 18
money = 10
count_toys = 0
sum = 0
count_bro = 0

for i in range(1, age + 1):
    if i % 2 != 0:
        count_toys += 1
    else:
        count_bro += 1
        sum = sum + money
        money += 10

saved_money = sum + (count_toys * toy_price) - count_bro
diff = abs(saved_money - price_wash_machine)
if saved_money >= price_wash_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
