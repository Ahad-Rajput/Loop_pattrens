"""

for n = 5

     12345
1    *
2    **
3    ***
4    ****
5    *****

"""

n = int(input("enter n: "))

row = 1
while row <= n:
    col = 1
    while col <= row:
        print('*', end="")
        col += 1
    print()
    row += 1