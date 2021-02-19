T1 = 16 # Tab for displaying base-10 addresses
T2 = 17 # Tab for displaying base-2 addresses

clamp_byte = lambda b: max(0, min(b, 255))        # Returns a clamped value between 0 and 255
clamp_mask = lambda m: max(0, min(m, 32))         # Returns a clamped value between 0 and 32
dot_sep = lambda l: '.'.join(map(str, l))         # Returns a dot-separated list values
to_bin = lambda x: '{:08b}'.format(x)             # Returns a formatted binary value
bin_dot_sep = lambda l: '.'.join(map(to_bin, l))  # Returns a dot-separated binary list values

def ip_calculator(inp):
    if inp in ['', 'help']:
        print('Command syntax: ip <ip-address>/<bitmask> (example: ip 192.168.1.1/24)\n')
        return
    inp = inp.split('/')
    if len(inp) > 2:
        print('Incorrect input! Type "ip" or "ip help" to see command help\n')
        return
    else:
        try:
            ip = list(map(int, inp[0].split('.')))
            if len(ip) > 4:
                print('IP address must contain 4 octets!\n')
                return
            else:
                while len(ip) < 4:
                    ip.append(0)
            ip = [clamp_byte(i) for i in ip]
        except:
            print('Incorrect IP-address!\n')
            return
        try:
            bitmask = clamp_mask(int(inp[1]))
        except:
            print('Incorrect bitmask!\n')
            return

    print('\n---------------------------- IP-Calculator ----------------------------')
    print('Address:'.ljust(T1), dot_sep(ip).ljust(T2), bin_dot_sep(ip), sep='')
    print('Bitmask:'.ljust(T1), bitmask, sep='')

    # Netmask
    netmask = [0, 0, 0, 0]
    for i in range(bitmask >> 3):
        netmask[i] = 255
    if bitmask < 32:
        netmask[bitmask >> 3] = ~(255 >> bitmask % 8) + 256
    print('Netmask:'.ljust(T1), dot_sep(netmask).ljust(T2), bin_dot_sep(netmask), sep='')

    # Wildcard
    wildcard = [~i + 256 for i in netmask]
    print('Wildcard:'.ljust(T1), dot_sep(wildcard).ljust(T2), bin_dot_sep(wildcard), sep='')

    # Network
    network = [ip[i] & netmask[i] for i in range(4)]
    print('Network:'.ljust(T1), dot_sep(network).ljust(T2), bin_dot_sep(network), sep='')
    
    # Broadcast
    if bitmask < 32:
        broadcast = [ip[i] | wildcard[i] for i in range(4)]
        print('Broadcast:'.ljust(T1), dot_sep(broadcast).ljust(T2), bin_dot_sep(broadcast), sep='')
    else:
        print('Broadcast:'.ljust(T1), 'N/A', sep='')
    
    hosts = 2 ** (32 - bitmask) - 2
    if hosts > 0:
        # HostMin > 0
        hostmin = network
        hostmin[3] += 1
        print('HostMin:'.ljust(T1), dot_sep(hostmin).ljust(T2), bin_dot_sep(hostmin), sep='')

        # HostMax > 0
        hostmax = broadcast
        hostmax[3] -= 1
        print('HostMax:'.ljust(T1), dot_sep(hostmax).ljust(T2), bin_dot_sep(hostmax), sep='')

        # Hosts/Net > 0
        print('Hosts/Net:'.ljust(T1), '{:,}'.format(hosts).ljust(T2), sep='', end='')
    else:
        print('HostMin:'.ljust(T1), 'N/A', sep='')   # HostMin = N/A
        print('HostMax:'.ljust(T1), 'N/A', sep='')   # HostMax = N/A
        print('Hosts/Net:'.ljust(T1), 'N/A'.ljust(T2), sep='', end='') # Hosts/Net = N/A

    # Finding network class
    octet = to_bin(network[0])
    if octet.startswith('0'):
        print('Class A')
    elif octet.startswith('10'):
        print('Class B')
    elif octet.startswith('110'):
        print('Class C')
    elif octet.startswith('1110'):
        print('Class D')
    elif octet.startswith('1111'):
        print('Class E - Experimental Address Space')
    
    print('-' * 71, '\n')
