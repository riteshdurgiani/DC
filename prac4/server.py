import threading
import socket
import datetime

server_time = input('Enter current time of time server : ')
server_time = datetime.datetime.strptime(server_time, "%H:%M")

HOST = '127.0.0.1'
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(4)
print('Time Server is listening...')

client_connections = []
client_time_values = []
skews = []


def service_client(client_connection, client_address, server_time):
    client_connection.send('Server Message : What is your current time (in HH:MM) ? '.encode())

    for client_connection in client_connections:
        client_time = client_connection.recv(1024).decode()
        if client_time == '':
            client_connections.remove(client_connection)
            client_connection.close()
            return
        client_time_values.append((client_connection, client_time))

    print()
    print('Client Clock Values Received :-')
    for client_connection, client_time in client_time_values:
        print(f'Client {client_connection.getpeername()} Clock : {client_time}')
        client_time = datetime.datetime.strptime(client_time, "%H:%M")
        skews.append((client_connection, int((client_time - server_time).total_seconds())))

    print()
    print('Skews Computed :-')
    avg_skew = 0
    for client_connection, skew in skews:
        print(f'Client {client_connection.getpeername()} : {skew} seconds')
        avg_skew += skew

    print()
    avg_skew /= (len(skews)+1)
    print(f'Average Skew by which to adjust server time : {avg_skew} seconds')
    server_time = server_time + datetime.timedelta(seconds=avg_skew)
    print('Adjusted Server Time : ', server_time.time())

    print()
    for client_connection, client_time in client_time_values:
        client_time = datetime.datetime.strptime(client_time, "%H:%M")
        adjustment = int((server_time - client_time).total_seconds())
        print(f'Sending Client {client_connection.getpeername()} Adjustment : {adjustment} seconds')
        msg = f'Server Message : Please adjust your clock by {adjustment} seconds...\nServer Message : Your clock value should be : {server_time.time()}'
        client_connection.send(msg.encode())


while True:
    client_connection, client_address = server.accept()
    client_connections.append(client_connection)
    print('Received connection from : ', client_address)

    thread = threading.Thread(target=service_client, args=(client_connection, client_address, server_time))
    thread.start()
