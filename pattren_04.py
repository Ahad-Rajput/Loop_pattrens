"""
-> for n = 4

4321
4321
4321
4321

"""


n = int(input("enter n: "))  # n for total no. of rows & cols

i=1   # iterator for outer while loop

"""
while i<=n:  # decides the no. of rows

    j=1   # iterator for inner loop

    while j<=n:  # decides the no. of cols

        print(n-j+1, end=" ")  #prints the counting according to pattren

        j+=1   # incremet j by 1

    print()   # for new line

    i+=1   # increment i by 1

"""

print("-------------------------------------------------------------------")

while i<=n:  # decides the no. of rows

    j=n   # iterator for inner loop

    while j>=1:  # decides the no. of cols

        print(j, end=" ")  #prints the counting according to pattren

        j-=1   # decrement j by 1

    print()   # for new line

    i+=1   # increment i by 1
