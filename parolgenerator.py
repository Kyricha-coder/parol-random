import random
import time
chars = "abcdefghijklmnopqrstuvwxyz1234567890!@';:#№%ABCDEFGHIJKLMNOPQRSTUVWXYZ`~?*()-_=+[]{}<>|/\\,^&$"
password = ""
while True:
    password = password + random.choice(chars)
    print(password)
time.sleep(1)