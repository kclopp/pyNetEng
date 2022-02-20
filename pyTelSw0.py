'''
Template from https://docs.python.org/3/library/telnetlib.html then edited.
'''

import getpass
import telnetlib

HOST = "192.168.0.10"
user = input("Enter your telnet account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"en\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")

tn.write(b"vlan 2\n")
tn.write(b"name Python_VLAN_2\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))