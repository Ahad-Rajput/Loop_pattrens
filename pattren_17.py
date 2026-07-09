"""
for n = 4

    1 2 3 4

1   A 
2   B C
3   C D E
4   D E F G

"""

n = int(input("enter n: "))


row=1
while(row<=n):
    col=1
    ch = 65
    while(col<=row):
        print(chr(ch+row-1), end=" ")
        col += 1
        ch += 1
    print()
    row += 1

