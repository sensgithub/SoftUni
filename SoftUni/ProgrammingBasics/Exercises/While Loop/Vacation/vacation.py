needed_cash = float(input())
aval_cash = float(input())

days_count = 0
spend_count = 0

while aval_cash < needed_cash and spend_count < 5:
    input_text = input()
    cash = float(input())
    days_count += 1

if input_text == "spend":
    aval_cash -= cash
    spend_count += 1
    if aval_cash < 0:
        aval_cash = 0
elif input_text == "save":
    aval_cash += cash
    spend_count = 0

if spend_count == 5:
    print("You can't save the money.")
    print(days_count)

if aval_cash >= aval_cash:
    print(f'You saved the money for {days_count} days.')
