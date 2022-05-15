price_tour = float(input())
puzzles = int(input())
count_dolls = int(input())
count_teddy_bears = int(input())
count_minions = int(input())
count_LKW = int(input())

total_spent = (puzzles * 2.60) + (count_dolls * 3) + (count_teddy_bears * 4.10) + (count_minions * 8.20) + (count_LKW * 2)
count_total = puzzles + count_dolls + count_teddy_bears + count_minions + count_LKW

if count_total >= 50:
    total_spent = total_spent * 0.75  # 75 %

total_spent = total_spent - (total_spent * 0.10)  # 10 %
# total_spent = total_spent * 0.90

diff = abs(total_spent - price_tour)

if total_spent > price_tour:
    print(f"Yes! {diff} lv left.")
else:
    print(f"Not enough money! {diff} lv needed.")
