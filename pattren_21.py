"""

for n = 4

    1 2 3 4

1   * * * *
2     * * *
3       * *
4         *

"""

n = int(input("enter n: "))

row = 1

while row <= n:
    space = row - 1
    while space:
        print(" ", end=" ")
        space -= 1
    col = n - row + 1
    while col:
        print('*', end=" ")
        col -= 1
    print()
    row += 1