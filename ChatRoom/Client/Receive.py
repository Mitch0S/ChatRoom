import requests
import os
import time

os.system("clear")
address = input("Please enter the server address: ")
port = input("Please enter the server port: ")
while True:
    try:
        postTo = (("http://{}:{}/get/")).format(address, port)
        chat = requests.post(postTo)
        chats = chat.json()
        time.sleep(0.5)
        messages = chats.split("=+-=-+-")
        os.system("clear")
        for i in messages:
            print(i)
    except:
        print("An error has ocurred, continuing.")
