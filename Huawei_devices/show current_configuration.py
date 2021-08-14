from netmiko import ConnectHandler
import time
start_time = time.time()
device = {
    'device_type': "cisco_ios_telnet",
    'host': '10.0.0.1',
    'username': 'username',
    'password': 'password',
    'port': '23',
}
connection = ConnectHandler(**device)

output = connection.send_command_expect('display cur', expect_string='---- More ----' )

more = '---- More ----'
while more:
    output = connection.send_command_timing(' ', strip_prompt=True, strip_command=False, max_loops=100, normalize=False)
    print(output)
    if 'return' in output:
        more = False
connection.disconnect()
print("--- %s seconds ---" % (time.time() - start_time))
