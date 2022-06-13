cake_length = int(input())
cake_width = int(input())

pieces_amount = cake_width * cake_length

input_line = input()
no_more_pieces = False

while input_line != "STOP":
    current_pieces = int(input_line)
    pieces_amount = pieces_amount - current_pieces

    if pieces_amount <= 0:
        no_more_pieces = True
        break
    input_line = input()

if no_more_pieces:
    print(f"No more cake left! You need {abs(pieces_amount)} pieces more.")
else:
    print(f"{abs(pieces_amount)} pieces are left.")
