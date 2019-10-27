#!/usr/bin/python

import base64
import time

print("Hackersifu Base64 Super Decoder Ring")
time.sleep(1)
secret = raw_input("Base64 encoded value? ")
print("Coming right up...")
time.sleep(1)
print("Here is the value: " + base64.b64decode(secret))
print("The value is above this line. Thanks!")
sys.exit(0)