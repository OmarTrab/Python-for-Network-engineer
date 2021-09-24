from netmiko import ConnectHandler

device ={
    'device_type': 'huawei',
    'host': '10.0.0.1',
    'username': 'user',
    'password': 'password',
    'port':'22'
}

connect = ConnectHandler(**device)
def config_mode (self,config_command='system-view'):
    return config_mode()
  
commands = ['vlan batch 25 26 27 28 29 30',
            'vlan 25'
            'description prova'
            'vlan 26',
            'description Vlan prova1',
            'vlan 27',
            'description prova2',
            'vlan 28',
            'description prova3',
            'vlan 29',
            'description prova4',
            'vlan 30',
            'description prova5']
output = connect.send_config_set(commands)

def exit_config_mode (self,exit_config='return', pattern='>'):
    return exit_config_mode()

output2 = connect.send_command_expect('save', expect_string = 'Y')
if 'y' in output2:
    output3 = connect.send_config_set('y')
connect.disconnect()
