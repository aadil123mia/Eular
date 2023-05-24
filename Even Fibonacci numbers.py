def fibonacci_sum(limit):
    # Initialize variables
    sum = 0
    a, b = 1, 2

    # Generate Fibonacci sequence and sum even terms
    while a <= limit:
        if a % 2 == 0:
            sum += a
        a, b = b, a + b

    return sum

# Calculate the sum with a limit of four million
result = fibonacci_sum(4000000)
print(result)