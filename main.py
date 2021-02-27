'''

This is example program where used all of the scripts I created

'''

import subprocess

utilities = {
    'ip': 'ipcalc.py',
    'pf': 'primefactor.py',
    'base': 'base.py'
}

help = {
    'ip': 'IP-Calculator',
    'pf': 'Prime Factorization',
    'base': 'Base'
}

print('Python utilities by Zepten')
print('Type <help> to see list of all commands')

while True:
    inp = input('\n>>> ')
    if inp == 'quit':
        quit()
    elif inp == 'help':
        print('Type <utility name> -h to see more information about specific utility\n')
        print('Utilities:')
        for i in help:
            print('  ', i.ljust(10), help[i], sep='')
        print('\nCommands:')
        print('  ', 'help'.ljust(10), 'Show this help message', sep='')
        print('  ', 'quit'.ljust(10), 'Quit the program', sep='')
    else:
        try:
            command = inp.split()
            program = utilities[command[0]]
            args = command[1:]
            process = subprocess.Popen([program, *args], shell=True)
            code = process.wait()
        except:
            print('There is no such command! Type <help> to see list of all commands')
