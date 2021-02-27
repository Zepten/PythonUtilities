import argparse

T1 = 12 # Tab for displaying base-10 addresses
T2 = 17 # Tab for displaying base-2 addresses

clamp_byte = lambda b: max(0, min(b, 255)) # Returns a clamped number value between 0 and 255
clamp_mask = lambda m: max(0, min(m, 32))  # Returns a clamped number value between 0 and 32
to_bin = lambda x: '{:08b}'.format(x)      # Returns a string of formatted binary value

# Returns a string of dot-separated list values
def dot_sep(l):
    if l == 'N/A':
        return l
    else:
        return '.'.join(map(str, l))

# Returns a string of dot-separated binary list values
def bin_dot_sep(l):
    if l == 'N/A':
        return l
    else:
        return '.'.join(map(to_bin, l))

# Argument parser
parser = argparse.ArgumentParser(description='IP-calculator')

# Positional arguments
parser.add_argument('address', type=str,        help='IPv4 address. Contains 4 dot-separated octets (example: 192.168.0.1)')
parser.add_argument('bitmask', type=int,        help='Number of netmask (0-32)')

# Optional arguments
parser.add_argument('-a', '--all',              help="Print all network properties", action='store_true')
parser.add_argument('-m', '--mask',             help="Print netmask", action='store_true')
parser.add_argument('-wc', '--wildcard',        help="Print wildcard", action='store_true')
parser.add_argument('-net', '-n', '--network',  help="Print network address", action='store_true')
parser.add_argument('-bc', '-b', '--broadcast', help="Print broadcast address", action='store_true')
parser.add_argument('-hmin', '--hostsmin',      help="Print min host address in network", action='store_true')
parser.add_argument('-hmax', '--hostsmax',      help="Print max host address in network", action='store_true')
parser.add_argument('--hosts',                  help="Print number of hosts per network", action='store_true')
parser.add_argument('-c', '--netclass',         help="Print network class", action='store_true')

# Argument parsing
args = parser.parse_args()

# IP parsing
ip = list(map(int, args.address.split('.')))

if len(ip) > 4:
    print('IP address must contain 4 octets (bytes)!')
    quit()
else:
    while len(ip) < 4:
        ip.append(0)

ip = [clamp_byte(i) for i in ip]

# Bitmask parsing
bitmask = clamp_mask(args.bitmask)

# Print parsed and clamped parameters
print()
print('Address:'.ljust(T1), dot_sep(ip).ljust(T2), bin_dot_sep(ip), sep='')
print('Bitmask:'.ljust(T1), bitmask, sep='')

# Netmask
netmask = [0, 0, 0, 0]
for i in range(bitmask >> 3):
    netmask[i] = 255
if bitmask < 32:
    netmask[bitmask >> 3] = ~(255 >> bitmask % 8) + 256

if args.mask or args.all:
    print('Netmask:'.ljust(T1), dot_sep(netmask).ljust(T2), bin_dot_sep(netmask), sep='')

# Wildcard
wildcard = [~i + 256 for i in netmask]

if args.wildcard or args.all:
    print('Wildcard:'.ljust(T1), dot_sep(wildcard).ljust(T2), bin_dot_sep(wildcard), sep='')

# Network
network = [ip[i] & netmask[i] for i in range(4)]

if args.network or args.all:
    print('Network:'.ljust(T1), dot_sep(network).ljust(T2), bin_dot_sep(network), sep='')

# Broadcast
if bitmask < 32:
    broadcast = [ip[i] | wildcard[i] for i in range(4)]
else:
    broadcast = 'N/A'

if args.broadcast or args.all:
    print('Broadcast:'.ljust(T1), dot_sep(broadcast).ljust(T2), bin_dot_sep(broadcast), sep='')

# Hosts
hosts = 2 ** (32 - bitmask) - 2

if hosts > 0:
    # HostMin
    hostmin = network
    hostmin[3] += 1

    # HostMax
    hostmax = broadcast
    hostmax[3] -= 1
else:
    hostmin = 'N/A'
    hostmax = 'N/A'
    hosts = 'N/A'

if args.hostsmin or args.all:
        print('HostMin:'.ljust(T1), dot_sep(hostmin).ljust(T2), bin_dot_sep(hostmin), sep='')

if args.hostsmax or args.all:
    print('HostMax:'.ljust(T1), dot_sep(hostmax).ljust(T2), bin_dot_sep(hostmax), sep='')

if args.hosts or args.all:
    if (hosts == 'N/A'):
        print('Hosts/Net:'.ljust(T1), hosts.ljust(T2), sep='')
    else:
        print('Hosts/Net:'.ljust(T1), '{:,}'.format(hosts).ljust(T2), sep='')

# Network class
if args.netclass or args.all:
    octet = to_bin(network[0])
    print('Class:'.ljust(T1), end='')
    if octet.startswith('0'):
        print('A')
    elif octet.startswith('10'):
        print('B')
    elif octet.startswith('110'):
        print('C')
    elif octet.startswith('1110'):
        print('D')
    elif octet.startswith('1111'):
        print('E - Experimental Address Space')
