import ipcalc
import primefactor

def help():
    print('\nAvailable commands:')
    print('ip - IP-Calculator')
    print('pf - Prime Factorization')
    print('Type command to see help for command\n')

print('Python utilities by Zepten')
print('Type "help" to see available commands\n')

while True:
    inp = input('> ').lower().lstrip(' ').rstrip(' ')
    if inp == 'quit':
        quit()
    elif inp == 'help':
        help()
    elif inp.startswith('ip'):
        inp = inp.replace('ip', '').lstrip(' ').rstrip(' ')
        ipcalc.ip_calculator(inp)
    elif inp.startswith('pf'):
        inp = inp.replace('pf', '').lstrip(' ').rstrip(' ')
        primefactor.prime_factorization(inp)
    elif inp == 'command':
        print('Very smart!\n')
    else:
        print('Unknown command\n')
