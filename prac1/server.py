import socket

HOST = '127.0.0.1'
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(1)
print('Server is listening...')
client_connection, client_address = server.accept()
print('Received connection from client : ', client_address)

while True:
    request = client_connection.recv(1024).decode()
    if request == 'done':
        break
    response = str(eval(request))

    print('Computing ', request)
    print('Result computed : ', response)
    print('Sending result to client...')

    client_connection.send(response.encode())
    print()

client_connection.close()
