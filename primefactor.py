def line():
    print("-" * 61)


print("-------------------- Prime factorization --------------------")
print("Input natural numbers to see the result (like 1, 2, 3, etc.)")
line()

while True:
    try:
        N = n = int(input("Input: "))
    except:
        print("Incorrect input!")
        line()
        continue
    if n < 1:
        print("Input only natural numbers!")
        line()
        continue
    elif n == 1:
        print("Didn't you know that 1 is prime? =)")
        line()
        continue
    prime = 2
    primes = []
    while prime <= n:
        if n % prime == 0:
            primes.append(prime)
            n //= prime
        else:
            prime += 1
    # Factors
    print(f"Factors: {N} =", " * ".join(str(p) for p in primes))
    # Set of powers
    primes = [[i, primes.count(i)] for i in set(primes)]
    primes.sort()
    print(f"Short:   {N} =",
          " * ".join((f"{p[0]}^{p[1]}" if p[1] > 1 else str(p[0])) for p in primes))
    line()
