width = int(input())
length = int(input())
height = int(input())

volume = width * length * height

sum_boxes = 0

input_line = input()

while input_line != "Done":
    boxes = int(input_line)

    sum_boxes += boxes

    if sum_boxes >= volume:
        break

    input_line = input()

if sum_boxes >= volume:
    print(f"None more free space! You need {abs(sum_boxes - volume)} Cubic meters more.")
else:
    print(f"{abs(sum_boxes - volume)} Cubic meters left.")
