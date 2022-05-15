budget = float(input())
video_count = int(input())
cpu_count = int(input())
ram_count = int(input())

video_sum = video_count * 250
cpu_sum = cpu_count * (video_sum * 0.35)
ram_sum = ram_count * (video_sum * 0.10)

all_sum = video_sum + cpu_sum + ram_sum
if video_count > cpu_count:
    all_sum = all_sum * 0.85

diff = abs(budget - all_sum)
if all_sum <= budget:
    print(f"You have {diff:.2f} lv left!")
else:
    print(f"Not enough money! You need {diff:.2f} lv more!")
