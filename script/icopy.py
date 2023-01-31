#!/usr/bin/python3

from paramiko import SSHClient
import paramiko
from scp import SCPClient

#scp -P 2222 controlnews.js raj@gator1417.hostgator.com:~/public_html/test1/home/js

def putOnceDay():
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('gator1417.hostgator.com',2222,'raj','597FUBNsOJob')
    with SCPClient(client.get_transport()) as scp:
        scp.put('/mnt/c/Users/schro/projects/biocharhub/',recursive=True,remote_path='~/public_html/biocharhub/')


putOnceDay()