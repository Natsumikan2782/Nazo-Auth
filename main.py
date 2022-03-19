import json
import time
import requests

print("Welcome to Auth")
time.sleep(1)
print("Please typing to username")
uname = input()
print("Please typing to password")
pas = input()
print("Authentication...")

try:
    r = requests.get('https://pastebin.com/raw/SGgRpnWD')
    date = r.json()
        
    if uname in date["users"]:
        if pas in date["pass"]:
            print("COMPLATE!")
        
        else:
            print("\nInvalid Username or password")
        
    else:
        print("\nInvalid Username or password")
    
except Exception:
    print("\nCAN'T CONNECTION TO AUTH-SERVER")
