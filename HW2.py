# Programming Language : PYTHON
import random


def fibonacci(n):
    # Finds the nth fibonacci number. So if n is 2, the output is 1 and if n is 6, output is 8.
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def print_fibonacci(n):
    # Prints all fibonacci numbers that are less than n. So if n is 4, it prints 0,1,1,2,3.
    num = 0
    fib_num = 0
    fibonacci_numbers = []
    while fib_num < n:
        fib_num = fibonacci(num)
        if fib_num < n:
            fibonacci_numbers.append(str(fib_num))
        num += 1
    print(" ".join(fibonacci_numbers))


min_range = int(input("Please provide a positive integer (start range): "))
# Asks for the first number as an input.
max_range = int(input("Please provide a positive integer (end range): "))
# Asks for the second number as an input.

if max_range < min_range:
    # Checks if second input number is not less than first num
    raise Exception("The start_range cannot be greater than the end_range")

module_num = int(input("Please provide a positive integer: "))
# Asks for the third number as an input.

true_results = [i for i in range(min_range, max_range + 1) if module_num % i == 0]
# Saves all the number between range of min_range and Max_range which evaluates to true when % with third input

true_result_size = len(true_results)
# Finds the size of the list after populating it.

if true_result_size == 0:
    raise RuntimeError("No valid Boolean expressions for the given input.")

random_value = random.randint(0, true_result_size - 1)
# Non-deterministically choosing one of the value from the list.

print_fibonacci(true_results[random_value])
# Prints Fibonacci sequence which is less than the Non-deterministically chosen value from a list
