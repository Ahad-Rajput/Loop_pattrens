"""

for n = 5

1
22
333
4444
55555

"""

n = int(input("enter n: "))

row = 1
while row <= n:
    col = 1
    while col <= row:
        print(row, end="")
        col += 1
    print()
    row += 1