"""

for n = 4

       1
     1 2 1
   1 2 3 2 1
 1 2 3 4 3 2 1  


"""

n = int(input("enter n: "))

row = 1

while row <= n:
    space = n - row
    while(space):
        print(" ", end=" ")
        space -= 1
    
    col = 1
    while col <= row:
        print(col, end=" ")
        col += 1
    
    coll = row - 1
    while(coll):
        print(coll, end=" ")
        coll -= 1

    print()
    row += 1