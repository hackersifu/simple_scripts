#!/usr/bin/python3
 
import sys
import os
import time

print("HackerSifu's Quick & Nasty EC2 SSH Script!")
time.sleep(1)
host = input("What is the IP/Hostname you're trying to connect to? ")
key = input("What is the name of the PEM file you are using to connect? It must end in .pem: ")
print("Note: The PEM file needs to be in the directory where you're running this script.")
time.sleep(1)
TrueKey = os.path.exists(key)
if TrueKey is True:
    os.system("ssh ec2-user@" + host + " -i " + key)
else:
    print("There's no key you big dummy! Try again.")
