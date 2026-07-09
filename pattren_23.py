"""

for n = 4

    1 2 3 4

1         1
2       2 2 
3     3 3 3
4   4 4 4 4

"""

n = int(input("enter n: "))

row = 1
while row<=n:
    space = n - row
    while(space):
        print(" ", end=" ")
        space -= 1
    
    col = 1
    while col<=row:
        print(row, end=" ")
        col += 1
    print()
    row += 1