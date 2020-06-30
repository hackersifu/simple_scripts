#!/usr/bin/python3
 
import sys
import os
import time

print("HackerSifu's Prowler Wrapper Script!")
time.sleep(1)
print("Configuring the prerequisites for Prowler...")
time.sleep(1)
os.system("sudo apt-get update -y")
os.system("sudo apt-get install python3-pip -y")
os.system("pip3 install --upgrade pip")
os.system("pip3 install awscli detect-secrets -y")
os.system("sudo apt-get install jq -y")
os.system("git clone https://github.com/toniblyx/prowler")
print("The prerequisites should be configured. Moving on to running Prowler, and exporting the findings into a .csv file.")
time.sleep(1)
os.system("cd prowler && sudo ./prowler -M csv")
print("Check the prowler directory to find the csv file. Thanks!")
sys.exit()