"""
-> for n = 5

11111
22222
33333
44444
55555

"""


n = int(input("enter n: "))  # n for total no. of rows & cols

i=1   # iterator for outer while loop

while i<=n:  # decides the no. of rows

    j=1   # iterator for inner loop

    while j<=n:  # decides the no. of cols

        print(i, end=" ")  #prints the counting according to pattren

        j+=1   # incremet j by 1

    print()   # for new line

    i+=1   # increment i by 1

