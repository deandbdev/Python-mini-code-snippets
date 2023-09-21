# finds and prints the first 100 prime numbers
# Initialize variables
count = 0  # Count of prime numbers found
num = 2    # Starting number to check for primality

# Continue until we find the first 100 prime numbers
while count < 100: # change this if you need more than 100 or less
    is_prime = True

    # Check if the number is prime
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    # If the number is prime, print it and increment the count
    if is_prime:
        print(num)
        count += 1

    # Move to the next number
    num += 1
