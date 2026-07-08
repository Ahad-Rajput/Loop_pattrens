"""
-> for n = 5


     12345
1    *****
2    *****   
3    *****   
4    *****
5    *****

"""




n = int(input("Enter n: "))   #n for total no. of rows & cols

i=0   #iterator for outer while loop

while(i<n):  # decides the no. of rows
    
    j=0  #iterator for inner loop
    
    while(j<n): # decides the no. of cols
        
        print('*', end="")  # print * side by side
        
        j+=1 # incremet j by 1
    
    print() # for new line
    
    i+=1  # increment i by 1
