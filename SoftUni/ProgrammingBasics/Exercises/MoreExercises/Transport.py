kilometers = int(input())
time_of_day = input()
total = 0

if time_of_day == 'day':

    if kilometers <= 100 and kilometers < 20:
        total = (kilometers * 0.79) + 0.70
        print(f'{total:.2f}')

    elif 20 <= kilometers < 100:
        total = kilometers * 0.09
        print(f'{total:.2f}')

    else:
        total = kilometers * 0.06
        print(f'{total:.2f}')

else:

    if kilometers <= 100 and kilometers < 20:
        total = (kilometers * 0.90) + 0.70
        print(f'{total:.2f}')

    elif 20 <= kilometers < 100:
        total = kilometers * 0.09
        print(f'{total:.2f}')

    else:
        total = kilometers * 0.06
        print(f'{total:.2f}')
