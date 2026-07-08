"""
-> for n = 5

12345
12345
12345
12345
12345

"""


n = int(input("enter n: "))  # n for total no. of rows & cols

i=1   # iterator for outer while loop

while i<=n:  # decides the no. of rows

    j=1   # iterator for inner loop

    while j<=n:  # decides the no. of cols

        print(j, end=" ")  #prints the counting according to pattren

        j+=1   # incremet j by 1

    print()   # for new line

    i+=1   # increment i by 1

