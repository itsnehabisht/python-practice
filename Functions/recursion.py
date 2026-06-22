'''
 factorial(5) = 5 X 4 X 3 X 2 X 1
 factorial(n) = n X n-1 X..........X 2 X 1

factorial(n) = n * factorial(n-1) 
  '''

def factorial(n):
    if(n == 0 or n == 1):
        return 1
    return n * factorial(n-1)

n = int(input("enter a number: "))
print(f"the factorial of this number is: {factorial(n)}")