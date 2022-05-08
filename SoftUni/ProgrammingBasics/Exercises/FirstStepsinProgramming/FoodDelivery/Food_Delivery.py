chicken_menu = int(input())
fish_menu = int(input())
veg_menu = int(input())

price_chicken = chicken_menu * 10.35
price_fish = fish_menu * 12.4
price_veg = veg_menu * 8.15

all_menu_price = price_chicken + price_fish + price_veg

dessert = all_menu_price * 0.20

total_price = all_menu_price + dessert + 2.5

print(total_price)