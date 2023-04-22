import socket

HOST = '127.0.0.1'
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

msg = client.recv(1024).decode()
print(msg)
client_time = input('Enter current time : ')
client.send(client_time.encode())

response = client.recv(1024).decode()
print(response)
