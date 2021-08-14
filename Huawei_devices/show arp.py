from netmiko import ConnectHandler         #Let's import Netmiko library


device ={
    'device_type': 'huawei',
    'host': '10.0.0.1',
    'username': 'user1',
    'password': 'Test123',
    'port':'22'
}                                    #We created a dictionary where we specify the parameters of the device

'''

Let's assign the ConnectionHandler parameter to the ssh_connect
where we go to indicate the device we have previoulsy listed
'''
ssh_coonect = ConnectHandler(**device)

'''
Let's nested the ssh_connect into  the output variable where 
we utilize the .sendcommand function
'''
output = ssh_coonect.send_command('display arp')
print(output)                                          #show the output result

ssh_coonect.disconnect()                   #disconetting from device


