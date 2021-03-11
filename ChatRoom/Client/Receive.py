import requests
import os
import time

address = input("Please enter the server address: ")
port = input("Please enter the server port: ")
while True:
    postTo = (("http://{}:{}/get/")).format(address, port)
    requests.post(postTo)
    chat = requests.post(postTo)
    chats = str((chat.content))
    chats = chats.replace("b'", "")
    chats = chats.replace("'", "")
    chats = chats.split("-")
    time.sleep(1)
    os.system("clear")
    for message in chats:
        print(message)