'''
Working with netmiko to automate ssh configuration with Cisco Switch for 
learning purposes only

Opens external file to configure Cisco IOS
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
sw4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.0.14',
    'username': 'kevin',
    'password': 'cisco'
}
sw5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.0.15',
    'username': 'kevin',
    'password': 'cisco'
}
sw6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.0.16',
    'username': 'kevin',
    'password': 'cisco'
}

with open('iosv_confg') as f:
    lines = f.read().splitlines()
print(lines)

all_devices = [sw1, sw2, sw3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output) 

with open('iosv_core') as f:
    lines = f.read().splitlines()
print(lines)

all_devices = [sw1, sw2, sw3, sw4, sw5, sw6]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output) 
