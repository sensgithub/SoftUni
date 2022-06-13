book_name = input()

count = 0  # track how many books are checked

is_book_found = False

current_book = input()

while current_book != 'No More Books':
    if current_book == book_name:
        is_book_found = True
        print(f'You checked {count} book and found it.')
        break
    count += 1
    current_book = input()

if not is_book_found:
    print('The book you search is not here!')
    print(f'You checked {count} books.')
    