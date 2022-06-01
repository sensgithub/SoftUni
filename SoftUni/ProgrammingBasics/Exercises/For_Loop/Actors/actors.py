actor_name = input()
init_points = float(input())
count = int(input())

total_points = init_points
for i in range(1, count + 1):
    name = input()
    current_points = float(input())

    points = (len(name) * current_points) / 2
    total_points = total_points + points

    if total_points >= 1250.5:
        break

if total_points >= 1250.0:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    diff = 1250.5 - total_points
    print(f"Sorry, {actor_name} you {diff:.1f} more!")
