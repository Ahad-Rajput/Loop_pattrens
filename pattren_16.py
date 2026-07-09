"""
for n = 4

    1 2 3 4

1   A 
2   B C
3   D E F
4   G H I J

"""

n = int(input("enter n: "))


row=1
ch = 65
while(row<=n):
    col=1
    while(col<=row):
        print(chr(ch), end=" ")
        ch += 1
        col += 1
    print()
    row += 1

