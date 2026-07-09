"""
for n = 4

    1  2  3  4

1   D
2   C  D
3   B  C  D
4   A  B  C  D

"""


n = int(input("enter n: "))

row = 1
while row <= n:
    col = 1
    ch = 65
    while col <= row:
        print(chr(ch+n-row), end=" ")
        col += 1
        ch += 1
    print()
    row += 1 
