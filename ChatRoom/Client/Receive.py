import requests
import os
import time

address = input("Please enter the server address: ")
port = input("Please enter the server port: ")
while True:
    postTo = (("http://{}:{}/get/")).format(address, port)
    requests.post(postTo)
    chat = requests.post(postTo)
    chats = chat.json()
    time.sleep(1)
    messages = chats.split("")
    os.system("clear")
    for i in messages:
        print(i)
