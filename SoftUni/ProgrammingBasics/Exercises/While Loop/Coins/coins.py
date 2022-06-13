change = float(input())
coins_change = round(change * 100)

count_coins = 0

while True:

    if coins_change >= 200:  # 2lv
        coins_change -= 200
        count_coins += 1

    elif coins_change >= 100:
        coins_change -= 100
        count_coins += 1

    elif coins_change >= 50:
        coins_change -= 50
        count_coins += 1

    elif coins_change >= 20:
        coins_change -= 20
        count_coins += 1

    elif coins_change >= 10:
        coins_change -= 10
        count_coins += 1

    elif coins_change >= 5:
        coins_change -= 5
        count_coins += 1

    elif coins_change >= 2:
        coins_change -= 2
        count_coins += 1

    elif coins_change >= 1:
        coins_change -= 1
        count_coins += 1
