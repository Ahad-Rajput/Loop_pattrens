"""

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

"""


n = int(input("enter n: "))

row_1 = 1

while row_1<=n:
    space = n - row_1
    while(space):
        print(" ", end=" ")
        space -= 1
    
    col_1 = 1
    while col_1 <= row_1:
        print('*', end=" ")
        col_1 += 1
    
    col_2 = row_1 - 1
    while(col_2):
        print('*', end=" ")
        col_2 -= 1
    print()
    row_1 += 1

row_2 = 1
while row_2 <= n:
    space = 1
    while space <= row_2:
        print(" ", end=" ")
        space += 1
    
    col_3 = n - row_2
    while (col_3):
        print('*', end=" ")
        col_3 -= 1

    col_4 = n - row_2 - 1
    while (col_4>0):
        print('*', end=" ")
        col_4 -= 1
    print()
    row_2 += 1
