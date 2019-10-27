import base64
import time

print("Hackersifu Base64 Super Decoder Ring")
time.sleep(1)
secret = raw_input("Base64 encoded value? ")

base64.b64decode(secret)
print("Thanks!")
sys.exit(0)