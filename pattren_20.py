"""

for n = 4

    1 2 3 4

1   * * * *
2   * * *
3   * *
4   *

"""

n = int(input("enter n: "))

row = 1
while row <= n:
    col = row
    while col <= n:
        print('*', end=" ")
        col += 1
    print()
    row += 1

    
