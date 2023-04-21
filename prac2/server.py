import socket
import threading

HOST = '127.0.0.1'
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print('Server is listening...')

client_connections = []

def service_client(sender_connection, sender_address):
    while True:
        request = sender_connection.recv(1024).decode()
        print(f'Message received from {sender_address} : ', request)
        print('Sending message to other clients...')
        request = f'Message from {sender_address} : ' + request

        for client_connection in client_connections:
            if client_connection != sender_connection:
                client_connection.send(request.encode())

while True:
    client_connection, client_address = server.accept()
    client_connections.append(client_connection)
    print('Received connection from : ', client_address)

    thread = threading.Thread(target=service_client, args=(client_connection, client_address))
    thread.start()
