
"""

for n = 5

1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

"""


n = int(input("enter n: "))

row = 1
count = 0   # initialize count 

while row <= n:
    col = 1
    while col <= n:
        count +=1  # add 1 in count in every iteration
        print(count, end=" ")  # print the counting according to pattren
        col += 1
    print()
    row += 1