"""

for n = 5

1
2 3
3 4 5
4 5 6 7
5 6 7 8 9

"""

n = int(input("enter n: "))


row = 1
while row <= n:
    col = 1
    while col <= row:
        print(row+col-1, end=" ")  # (row + col - 1) => For starting the new row with that row number
        col += 1
    print()
    row += 1

print("------------------------------------------------------------------------")

"""
U can also make this pattren by adding new integer and give it the current row no.
For example:
    row = 1
    while row <= n:
        value = row
        col = 1
        while col <= row:
            print(value)
            value++
            col++
        row++

"""