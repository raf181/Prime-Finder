import csv
import timeit
import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    # Check divisibility by all numbers from 5 to the square root of num
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    
    return True

def find_largest_prime_with_digits(digits):
    largest_prime = 0
    execution_times = []
    for run in range(5):  # Perform the test five times to calculate an average time
        start_time = timeit.default_timer()
        prime = find_prime(digits)
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        execution_times.append(execution_time)

        if prime > largest_prime:
            largest_prime = prime

    average_time = sum(execution_times) / len(execution_times)
    return largest_prime, average_time, execution_times

def find_prime(digits):
    max_limit = 10 ** digits - 1
    min_limit = 10 ** (digits - 1)

    for num in range(max_limit, min_limit - 1, -1):
        if is_prime(num):
            return num

with open('prime_numbers.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    headers = ['Digits', 'Largest Prime', 'Average Time']
    for i in range(1, 6):
        headers.append(f'Run {i}')
    csv_writer.writerow(headers)

    for digits in range(1, 21):  # This loop tests for prime numbers with 0 to 20 digits
        largest_primes = []
        average_times = []
        all_execution_times = []
        for _ in range(5):  # Perform the tests five times
            largest_prime, average_time, execution_times = find_largest_prime_with_digits(digits)
            largest_primes.append(largest_prime)
            average_times.append(average_time)
            all_execution_times.append(execution_times)

        # Calculate the average of the five average times
        overall_average_time = sum(average_times) / len(average_times)

        # Create a row for this digit count in the CSV file
        row = [digits, max(largest_primes), overall_average_time]
        for i in range(5):  # Add individual execution times for each run
            row.append(all_execution_times[i][0])  # Change [0] to [1] for the second run, [2] for the third, etc.

        # Write the row to the CSV file
        csv_writer.writerow(row)

        # Print the results for this digit count
        print(f"Largest prime with {digits} digits - Largest Prime: {max(largest_primes)}")
        print(f"Average Time: {overall_average_time:.15f} seconds")
        for i, execution_time in enumerate(average_times):
            print(f"Individual Execution Time {i + 1}: {execution_time:.15f} seconds")
        print()

print("Results saved to prime_numbers.csv")