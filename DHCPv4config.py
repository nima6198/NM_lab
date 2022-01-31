#usr/bin/env/python
#importing modules
from netmiko import ConnectHandler
import time

def Router2():
    
    R2 = {
        'device_type':'cisco_ios',
        'ip': '198.51.100.18',
        'username': 'netman',
        'password': 'netman',
        'secret': 'netman'
        }

    print("Logged in SSH succesfully")
    print(R2)
    net_connect = ConnectHandler(**R2)
    config_commands1 = ['int f0/0', 'ip address dhcp','no shut','exit']
    net_connect.enable()
    outcome = net_connect.send_config_set(config_commands1)
    print(outcome)
    net_connect.disconnect()

def Router3():
    
    R3 = {
        'device_type':'cisco_ios',
        'ip': '198.51.100.19',
        'username': 'netman',
        'password': 'netman',
        'secret': 'netman'
        }

    print("Logged in SSH succesfully")
    print(R3)
    net_connect = ConnectHandler(**R3)
    config_commands1 = ['int f0/0', 'ip address dhcp','no shut','exit']
    net_connect.enable()
    outcome2 = net_connect.send_config_set(config_commands1)
    print(outcome2)
    net_connect.disconnect()

def Router4():
    
    R4 = {
        'device_type':'cisco_ios',
        'ip': '198.51.100.20',
        'username': 'netman',
        'password': 'netman',
        'secret': 'netman'
        }

    print("Logged in SSH succesfully")
    print(R4)
    net_connect = ConnectHandler(**R4)
    config_commands1 = ['int f0/0', 'ip address dhcp','no shut','exit']
    net_connect.enable()
    outcome3 = net_connect.send_config_set(config_commands1)
    print(outcome3)
    net_connect.disconnect()
    

Router2()
Router3()
Router4()
    



 
