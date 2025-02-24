
# Sieve of Eratosthenes
# coellect all primes under n
# O(n log (log n))
def get_prime(n):
    sieve = [True] * (n + 1)
    prime = []
    for i in range(2, n + 1):
        if sieve[i]:
            prime.append(i)
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return prime


# Sieve of Eratosthenes
# build prime table only
# O(n log (log n))
def prime_table(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve


# prime factorization
# O(sqrt(n))
def prime_fact(n):
    fact = []
    p = 2
    while p * p <= n:
        while n % p == 0:
            fact.append(p)
            n //= p
        p += 1
    if n != 1:
        fact.append(n)
    return fact


# check is prime or not
# O(sqrt(n))
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n >= 2
