""""

for n = 5

1    1 2 3 4 5 5 4 3 2 1
2    1 2 3 4 * * 4 3 2 1
3    1 2 3 * * * * 3 2 1
4    1 2 * * * * * * 2 1
5    1 * * * * * * * * 1

"""

n = int(input("enter n: "))

row = 1

while row <= n:
    col = 1
    while col <= (n-row+1):
        print(col,end=" ")
        col += 1
    star_1 = row - 1
    while(star_1):
        print("*", end=" ")
        star_1 -= 1
    star_2 = row - 1
    while(star_2):
        print("*", end=" ")
        star_2 -= 1
    coll = n - row + 1
    while coll:
        print(coll, end=" ")
        coll -= 1
    print()
    row += 1
    