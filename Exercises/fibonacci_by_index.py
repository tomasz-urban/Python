# Return Fibonacci number with given index
# fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

# First one is iterative search using a for loop

def fibonacci_iterative(n):
    if n < 0:
        return "The number has to be higher than 0!"
    elif n == 0:
        return 0
    else:
        a = 0
        b = 1
        for i in range(n-1):
            temp = a
            a = b
            b = temp + b
        return b


print(fibonacci_iterative(12))

# Second one is searching using recursion, so calling function by itself until it gets right answer

def fibonacci_recursive(n):
    if n < 0:
        return "The number has to be higher than 0!"
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


print(fibonacci_recursive(12))


