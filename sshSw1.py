'''
Working with netmiko to automate ssh configuration with Cisco Switch for 
learning purposes only
'''

from netmiko import ConnectHandler

sw1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.0.11',
    'username': 'kevin',
    'password': 'cisco'
}
sw2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.0.12',
    'username': 'kevin',
    'password': 'cisco'
}
sw3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.0.13',
    'username': 'kevin',
    'password': 'cisco'
}
all_devices = [sw1, sw2, sw3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (2,21):
        print ("Creating VLAN " + str(n))
        config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print (output) 
