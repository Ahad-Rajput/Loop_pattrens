"""
for n = 3

    1 2 3

1   A A A
2   B B B
3   C C C

"""

n = int(input("enter n: "))

ch = 65

row=0
while(row<n):
    col=0
    while(col<n):
        print(chr(ch), end=" ")
        col += 1
    print()
    ch += 1
    row += 1

