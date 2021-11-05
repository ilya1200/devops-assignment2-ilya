size = 7
char = "#"

for row in range(size):
    row_to_print = str()
    for col in range(size):
        if col == row or col == size-row-1:
            row_to_print += char
        else:
            row_to_print += " "
    print(row_to_print)
