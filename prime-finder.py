import time

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_largest_prime_with_digits(digits):
    start_time = time.time()
    max_limit = 10 ** digits - 1
    largest_prime = None

    for num in range(max_limit, 1, -1):
        if is_prime(num):
            largest_prime = num
            break

    end_time = time.time()
    execution_time = end_time - start_time

    return largest_prime, execution_time

for digits in range(2, 1001):  # Change the range to 1001 for 2 to 1000 digits
    largest_prime, execution_time = find_largest_prime_with_digits(digits)
    print(f"Largest prime with {digits} digits: {largest_prime}")
    print(f"Execution Time: {execution_time} seconds")
    print()
