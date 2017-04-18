#!/usr/bin/env python
"""
Controls autostarting of VM's on ESXI over SSH
"""

import sh

ip = ''
vmid = ''
start_action = ''
start_delay = ''
start_order = ''
stop_action = ''
stop_delay = ''
heartbeat = ''

while ip == '':
    ip = input('IP Address: ')
print('Please input the details of the VM to modify.')
print(sh.ssh(f"root@{ip}", "vim-cmd vmsvc/getallvms"))
while vmid == '':
    vmid = input('Vmid: ')
while start_action == '':
    start_action = input('Start Action (Start/Stop): ')
while start_delay == '':
    start_delay = input('Start Delay: ')
while start_order == '':
    start_order = input('Start Order: ')
while stop_action == '':
    stop_action = input('Stop Action (Stop/Suspend): ')
while stop_delay == '':
    stop_delay = input('Stop Delay: ')
while heartbeat == '':
    heartbeat = input('Wait for heartbeat(y/n): ')

print('Incorrect input can cause damage or unknown errors. Is all information correct?')
print(f'Start Action: {start_action}, Start Delay: {start_delay}, Start Order: {start_order}, Stop Action: {stop_action}, Stop Delay: {stop_delay}')
yn = input('y/N')
if yn.lower() == 'y' or yn.lower() == 'yes':
    print(sh.ssh(f'root@{ip}', f'hostsvc/autostartmanager/update_autostartentry {vmid} {start_action} {start_delay} {start_order} {stop_action} {stop_delay} {heartbeat}'))
else:
    print('No actions taken.')
