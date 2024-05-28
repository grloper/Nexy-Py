def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes(n):
    while True:
        if is_prime(n):
            yield n
        n += 1

def first_prime_over(n):
    prime_generator = primes(n)
    while True:
        prime = next(prime_generator)
        print(prime)
        
first_prime_over(1000000)