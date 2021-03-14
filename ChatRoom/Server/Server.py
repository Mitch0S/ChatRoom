import flask
from flask import request
from flask import jsonify

app = flask.Flask(__name__)

@app.route('/get/', methods=['POST'])
def get_config():
    chat = open("chat.txt", "r+").readlines()
    chats = ""
    for line in chat:
        chats = chats+"=+-=-+-"+(line).strip()
    #print(chats)
    return jsonify(chats)

@app.route('/post/', methods=['POST'])
def post_config():
    notAllowedCharacters = ["", " "]
    information = request.headers
    username = information["Username"]
    message = information["Message"]
    chat = open("chat.txt", "a+")
    if message in notAllowedCharacters:
        return jsonify("You entered an invalid message.")
    else:
        chat.write(("[{}]: {}\n").format(username, message))
        return jsonify("Chat successfully sent.")

@app.route('/new_conn/', methods=['POST'])
def new_conn():
    information = request.headers
    username = information["Username"]
    chat = open("chat.txt", "a+")
    chat.write(("{} has joined the chat!\n").format(username))
    return jsonify("Successfully joined the chat room.")

app.run(host='0.0.0.0', port=1312)
