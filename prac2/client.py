import socket
import threading

HOST = '127.0.0.1'
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    while True:
        response = client.recv(1024).decode()
        print(response)

thread = threading.Thread(target=receive_messages)
thread.start()

while True:
    request = input()
    client.send(request.encode())
