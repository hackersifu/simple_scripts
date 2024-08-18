import base64
import time

print("Hackersifu Base64 Super Decoder Ring")
time.sleep(1)

# Use input() instead of raw_input() for Python 3.x
secret = input("Base64 encoded value? ")

print("Coming right up...")
time.sleep(1)

# Decode the base64 string and ensure it's a proper string in Python 3.x
decoded_value = base64.b64decode(secret).decode('utf-8')

print("Here is the value: " + decoded_value)
print("The value is above this line. Thanks!")