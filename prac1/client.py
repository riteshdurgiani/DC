import socket

HOST = '127.0.0.1'
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    num1 = input('Enter operand 1 : ')
    operator = input('Enter operator (+,-,*,/) : ')
    num2 = input('Enter operand 2 : ')

    request = num1+operator+num2
    client.send(request.encode())

    response = client.recv(1024).decode()
    print('Result is : ', response)

    option = input('Continue? (y/n) : ')
    if option == 'n':
        client.send('done'.encode())
        break
    print()
