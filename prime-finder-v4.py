import csv
import time

# Define a function to check if a number is prime
def is_prime(num):
    # Base cases for 0, 1, 2, and 3
    if num <= 1:
        return False
    if num <= 3:
        return True
    # Check divisibility by 2 and 3
    if num % 2 == 0 or num % 3 == 0:
        return False
    # Check divisibility by numbers of the form 6k ± 1 up to the square root of num
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Define a function to find the largest prime number with a specified number of digits
def find_largest_prime_with_digits(digits):
    start_time = time.perf_counter()
    max_limit = 20 ** digits - 1

    for num in range(max_limit, 10 ** (digits - 1), -1):
        if is_prime(num):
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            return execution_time

# Create and open a CSV file for writing
with open('prime_numbers.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write the header row to the CSV file
    csv_writer.writerow(['Digits', 'Execution Time 1', 'Execution Time 2', 'Execution Time 3', 'Average Time'])

    for digits in range(2, 20):  # This loop tests for prime numbers with 2 to 19 digits
        execution_times = []
        for _ in range(3):  # Perform the test three times to calculate an average time
            execution_time = find_largest_prime_with_digits(digits)
            execution_times.append(execution_time)
        
        # Calculate the average execution time
        average_time = sum(execution_times) / len(execution_times)

        # Write the results for this digit count to the CSV file
        csv_writer.writerow([digits] + execution_times + [average_time])
        
        # Print the execution times and average time for this digit count
        print(f"Largest prime with {digits} digits - Execution Times: {execution_times}")
        print(f"Average Time: {average_time:.10f} seconds")
        print()

# Print a message indicating that the results have been saved to the CSV file
print("Results saved to prime_numbers.csv")
