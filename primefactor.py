def prime_factorization(inp):
    if inp in ['', 'help']:
        print('Command syntax: pf <number> (use natural numbers like 1, 2, 3, etc.)\n')
        return
    
    try:
        N = n = int(inp)
    except:
        print('Incorrect input! Type "pf" or "pf help" to see command help\n')
        return
    if n < 1:
        print('Input only natural numbers!\n')
        return
    elif n == 1:
        print("Didn't you know that 1 is prime? =)\n")
        return
    prime = 2
    primes = []
    while prime <= n:
        if n % prime == 0:
            primes.append(prime)
            n //= prime
        else:
            prime += 1
    
    # Factors
    print(f'\nFactors: {N} =', ' * '.join(str(p) for p in primes))

    # Set of powers
    primes = [[i, primes.count(i)] for i in set(primes)]
    primes.sort()
    print(f'Short:   {N} =',
          ' * '.join((f'{p[0]}^{p[1]}' if p[1] > 1 else str(p[0])) for p in primes))
    print()
