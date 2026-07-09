"""
for n = 3

    1 2 3

1   A B C
2   B C D
3   C D E

"""

n = int(input("enter n: "))


row=1
while(row<=n):
    col=1
    ch = 65
    while(col<=n):
        print(chr(ch+row-1), end=" ")
        col += 1
        ch += 1
    print()
    row += 1

