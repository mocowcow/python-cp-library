
# Sieve of Eratosthenes
# O(n log (log n))
def get_prime(n):
    sieve = [True]*(n+1)
    prime = []
    for i in range(2, n+1):
        if sieve[i]:
            prime.append(i)
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return prime


# build prime table
# sqrt(n) is enough for sieve
def prime_table(n):
    sieve = [True]*(n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return sieve


# prime factorization
def prime_fact(n):
    fact = []
    p = 2
    while p*p <= n:
        while n % p == 0:
            fact.append(p)
            n //= p
        p += 1
    if p != 1:
        fact.append(p)
    return fact
