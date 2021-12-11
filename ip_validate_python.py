import ipaddress
# script checks if ips are valid and if ip is part of a network
# ex : print(ip_check('192.168.0.0/24', '192.168.0.1'))


def ip_check(ip_net, ip):
    try:
        ip1 = ipaddress.ip_address(ip)
        ip2 = ipaddress.ip_network(ip_net)
        net = ip1 in ip2
        if net is False:
            raise ValueError('ip not valid')
    except ValueError:
        return False

    return True
