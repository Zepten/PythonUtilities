import argparse

# Argument parser
parser = argparse.ArgumentParser(description='Prime Factorization')

# Positional argument
parser.add_argument('number', type=int, help='Natural number')

# Optional argument
parser.add_argument('-a', '--all',    help='Represent as factors and powers', action='store_true')
parser.add_argument('-p', '--powers', help='Represent as powers (default: as factors)', action='store_true')

# Argument parsing
args = parser.parse_args()

# Number
N = n = args.number

if n < 1:
    print('Input only natural numbers!')
    quit()
elif n == 1:
    print("Didn't you know that 1 is prime? =)")
    quit()

prime = 2
primes = []
while prime <= n:
    if n % prime == 0:
        primes.append(prime)
        n //= prime
    else:
        prime += 1

print()

# Factors
if not args.powers or args.all:
    print('Factors:'.ljust(10), f'{N} = ', ' * '.join(str(p) for p in primes), sep='')

# Powers
if args.powers or args.all:
    primes = [[i, primes.count(i)] for i in set(primes)]
    primes.sort()
    print('Powers:'.ljust(10), f'{N} = ',
        ' * '.join((f'{p[0]}^{p[1]}' if p[1] > 1 else str(p[0])) for p in primes), sep='')
