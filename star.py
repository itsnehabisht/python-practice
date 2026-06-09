'''
***
* *
***
'''
# print the pattern

n = int (input("enter a number"))
for i in range(1, n+1):
    if(i==1 or i==n):  # first and last line
        print("*" * n, end= "")

    else: 
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end="")
    print(" ")