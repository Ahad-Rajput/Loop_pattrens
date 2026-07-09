"""

for n = 5

1
2 1
3 2 1
4 3 2 1
5 4 3 2 1

"""

n = int(input("enter n: "))


row = 1
while row <= n:
    col = 1
    while col <= row:
        print(row-col+1, end=" ")  
        col += 1
    print()
    row += 1
