#!/usr/bin/python3
 
import sys
import os
import time

print("HackerSifu's Quick & Nasty EC2 SSH Script!")
time.sleep(1)
host = input("What is the IP/Hostname you're trying to connect to? ")
ssh_user = input("What is the username for your EC2 instance? e.g. ubuntu, ec2user, root, etc ")
key = input("What is the name of the PEM file you are using to connect? It must end in .pem: ")
print("Note: The PEM file needs to be in the directory where you're running this script.")
time.sleep(1)
#The os.path.exists checks if the file is in place. If it is, it returns True. If not, it returns False.
TrueKey = os.path.exists(key)
if TrueKey is True:
    os.system("ssh " + ssh_user + "@" + host + " -i " + key)
else:
    print("There's no key you big dummy! Try again.")
