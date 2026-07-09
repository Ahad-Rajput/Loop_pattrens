"""

for n = 4

    1 2 3 4

1         1
2       2 3 
3     4 5 6
4   7 8 9 10

"""

n = int(input("enter n: "))

row = 1
count = 1
while row<=n:
    space = n - row
    while(space):
        print(" ", end=" ")
        space -= 1
    
    col = 1
    while col<=row:
        print(count, end=" ")
        col += 1
        count += 1
    print()
    row += 1