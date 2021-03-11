import requests

username = input("Please enter your username: ")
address = input("Please enter the server address: ")
port = input("Please enter the server port: ")
while True:
    message = input("Message: ")
    headers = {
        "Username": username,
        "Message": message
    }
    request.post(("http://{}:{}/post/").format(address, port)