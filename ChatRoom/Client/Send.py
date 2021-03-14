import requests
import os
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
    username = input("Please enter your username: ")
    address = input("Please enter the server address: ")
    port = input("Please enter the server port: ")

credidentials = {
    "Username": username
}
requests.post(("http://{}:{}/new_conn/").format(address, port), headers=credidentials)

print(("Hello, {}, welcome to Mitch's Chatroom!").format(username))
while True:
    try:
        message = input("Message: ")
        headers = {
            "Username": username,
            "Message": message
        }
        requests.post(("http://{}:{}/post/").format(address, port), headers=headers)
    except:
        print("An error has ocurred, retrying...")
