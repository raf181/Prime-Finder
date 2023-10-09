import csv
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
    csv_writer.writerow(['Digits', 'Execution Time 1', 'Execution Time 2', 'Execution Time 3', 'Average Time'])

    for digits in range(2, 20):  # Change the range to 1001 for 2 to 1000 digits
        execution_times = []
        for _ in range(3):
            execution_time = find_largest_prime_with_digits(digits)
            execution_times.append(execution_time)
        
        average_time = sum(execution_times) / len(execution_times)

        csv_writer.writerow([digits] + execution_times + [average_time])
        print(f"Largest prime with {digits} digits - Execution Times: {execution_times}")
        print(f"Average Time: {average_time:.10f} seconds")
        print()

print("Results saved to prime_numbers.csv")
