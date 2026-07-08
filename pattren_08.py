"""

for n = 5

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

"""

n = int(input("enter n: "))

count = 1

row = 1
while row <= n:
    col = 1
    while col <= row:
        print(count, end=" ")
        count += 1
        col += 1
    print()
    row += 1