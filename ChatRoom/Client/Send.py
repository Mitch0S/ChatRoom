import requests
import os

os.system("clear")
username = input("Please enter your username: ")
address = input("Please enter the server address: ")
port = input("Please enter the server port: ")

credidentials = {
    "Username": username
}
requests.post(("http://{}:{}/new_conn/").format(address, port), headers=credidentials)

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
