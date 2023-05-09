import socket
import threading

def receive_messages():
    while True:
        try:
            message = client_socket.recv(BUFFER_SIZE)
            if message:
                print(message.decode())
        except:
            client_socket.close()
            break



SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000
BUFFER_SIZE = 4096

username = input('Enter your nickname: ')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))
client_socket.send(username.encode())

receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

while True:
    message = input()
    if message == 'quit':
        break
    client_socket.send(message.encode())

client_socket.close()