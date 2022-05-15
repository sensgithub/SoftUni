budget = float(input())
count_statists = int(input())
price_clothing_one = float(input())

decor = budget * 0.10
all_clothes_price = count_statists * price_clothing_one

if count_statists > 150:
    all_clothes_price = all_clothes_price * 0.90

expenses = decor + all_clothes_price
diff = abs(expenses)
