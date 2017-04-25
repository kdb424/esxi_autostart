#!/usr/bin/env python
"""
Enables autostarting of VM's on ESXI over SSH
"""
import sh

ip = ''
enable = ''

while ip == '':
    ip = input('IP Address: ')
while enable == '':
    enable = input('Enable: (y/n)')
if enable.lower() == 'y' or enable.lower() == 'yes':
    print(sh.ssh(f"root@{ip}", "vim-cmd /hostsvc/autostartmanager/enable_autostart true"))
elif enable.lower() == 'n' or enable.lower() == 'no':
    print(sh.ssh(f"root@{ip}", "vim-cmd /hostsvc/autostartmanager/enable_autostart false"))
else:
    print('Input not recognized. No changes were made to the system.')
