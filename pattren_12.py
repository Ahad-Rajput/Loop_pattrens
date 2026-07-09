"""
for n = 3

    1 2 3

1   A B C
2   A B C
3   A B C

"""

n = int(input("enter n: "))


row=0
while(row<n):
    col=0
    ch = 65
    while(col<n):
        print(chr(ch), end=" ")
        col += 1
        ch += 1
    print()
    row += 1

