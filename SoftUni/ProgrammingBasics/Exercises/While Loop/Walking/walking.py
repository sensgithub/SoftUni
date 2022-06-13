input_line = input()
goal = 10000
sum_steps = 0

while input_line != 'Going home':
    steps = int(input_line)
    sum_steps += steps
    if sum_steps >= goal:
        break
    input_line = input()

if input_line == 'Going home':
    new_steps = int(input())
    sum_steps += new_steps

if sum_steps >= goal:
    print("Goal reached! Good job!")
    print(f"{abs(goal - sum_steps)} steps over the goal!")
else:
    print(f'{abs(goal - sum_steps)} more steps to reach goal.')
