from __future__ import absolute_import, division, print_function
import netmiko


apparati = '''
192.168.1.1
192.168.1.2
192.168.1.3
192.168.1.4
192.168.1.5
192.168.1.6
192.168.1.7
192.168.1.8
192.168.1.9
192.168.1.10
'''.strip().splitlines()

device_type = 'huawei'
username = 'user_huawei'
password = 'password123'
port = 22

netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException,
                      netmiko.ssh_exception.NetMikoAuthenticationException)


for devices in apparati:
    try:
        print('+' * 80)
        print('Connecting to device:', devices)
        connessione = netmiko.ConnectHandler(ip=devices, device_type=device_type, username=username, password=password,
                                             port=port)
        output = connessione.send_command('display bgp peer')
        if 'Idle' in output:
            print('Link down, peer in Idle state')
        elif 'Connect' in output:
            print('Link down, peer in Connect state')
        elif 'Active' in output:
            print('Link down, peer in Active state')
        else:
            print('Stable links!')
            
        connessione.disconnect()
        
    except netmiko_exceptions as fail:
        print('Failed to ', devices, fail)

