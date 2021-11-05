num = 5
char = "#"

for row in range(1, num+1):
    row_print = str()
    for col in range(0, row):
        row_print = row_print + char
    print(row_print)
