"""
for n = 3

    1 2 3

1   A 
2   B B
3   C C C

"""

n = int(input("enter n: "))


row=1
ch = 65
while(row<=n):
    col=1
    while(col<=row):
        print(chr(ch), end=" ")
        col += 1
    print()
    ch += 1
    row += 1

