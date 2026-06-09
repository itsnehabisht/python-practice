'''
***
**
*
'''
#print the pattern
# n = int(input("enter a number: "))
# for i in range(1, n+1):
#     print("*"* (n-i+1), end= "")
#     print(" "* (i-1), end= "")
#     print()

def pattern(n):
    if(n==0):
        return 
    print("*"*n)
    pattern(n-1)

pattern(3)