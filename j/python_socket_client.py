'''
    Python Socket编程
'''
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",8000))
client.send("skyl",encode("utf8"))

