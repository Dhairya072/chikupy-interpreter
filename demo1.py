# create a function that calculates fibonacci number at the given index

def fib(n):
    prev2 = 0
    prev1 = 1
    for i in range(n):
        if(i == 0):
            print(prev2, end = " ")
        elif(i == 1):
            print(prev1, end = " ")
        else:
            sum1 = prev1 + prev2
            print(sum1, end = " ")
            prev2 = prev1
            prev1 = sum1
    # create a function that calculates factorial of the given number


def fact(n):
    ans = 1
    while(n >= 1):
        ans *= n
        n = n - 1
    return ans
    # create a function that calculates the sum of the given numbers


def sum(*args):
    
    pass

    # create a function that calculates the product of the given numbers


def product(*args):

    pass

    # create a function that calculates the average of the given numbers


def average(*args):
    num = 0
    n = 0

    for arg in args:
        num += arg
        n = n+1
    return num/n
    

fib(10)


print("demo issue")