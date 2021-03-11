import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/get/', methods=['POST'])
def get_config():
    chat = open("chat.txt", "r+").readlines()
    chats = ""
    for line in chat:
        chats = chats+"-"+(line).strip()
    #print(chats)
    return chats

@app.route('/post/', methods=['POST'])
def post_config():
    information = request.headers
    username = information["Username"]
    message = information["Message"]
    chat = open("chat.txt", "a+")
    chat.write(("[{}]: {}\n").format(username, message))
    return "Successfully send the chat"


app.run(host='0.0.0.0', port=1312)