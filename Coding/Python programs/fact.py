n=int(input("Enter a number: "))
def factorial(n):
    global fact
    if n == 0 or n == 1:
        return 1
    else:
        fact = n * factorial(n - 1)
        return fact 

factorial(n)
print(f"The factorial of {n} is: {fact}")   
        