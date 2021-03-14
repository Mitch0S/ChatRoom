import requests
import os
import time

os.system("clear")

try:
    file = open("Desktop/ChatRoom/INFORMATION.txt", "r+")
    for line in file.readlines():
        line = line.split(": ")
        if line[0] == "ADDRESS":
            address = line[1].strip()
        if line[0] == "PORT":
            port = line[1].strip()
        if line[0] == "USERNAME":
            username = line[1].strip()
except:
    print("Unable to find credidentials file.\n------------------------------------")
    address = input("Please enter the server address: ")
    port = input("Please enter the server port: ")

while True:
    try:
        postTo = (("http://{}:{}/get/")).format(address, port)
        chat = requests.post(postTo)
        oldChat = chat
        chats = chat.json()
        time.sleep(0.5)
        messages = chats.split("=+-=-+-")
        os.system("clear")
        for i in messages:
            print(i)
    except:
        print("An error has ocurred, continuing.")
