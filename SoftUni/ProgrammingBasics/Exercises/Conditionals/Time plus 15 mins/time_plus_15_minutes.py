hours = int(input())
mins = int(input())

total_time = (hours * 60) + mins + 15

hours_new = total_time // 60
mins_new = total_time % 60

if hours_new > 23:
    hours_new = 0

if mins_new < 10:
    print(f"{hours_new}:0{mins_new}")
else:
    print(f"{hours_new}:0{mins_new}")
