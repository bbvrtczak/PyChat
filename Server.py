import socket
import threading

def broadcast_message(message, sender):
    username = username_dict[sender]
    message_with_username = f"{username}: {message.decode()}"
    for client in clients:
        if client != sender:
            client.send(message_with_username.encode())


def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)
        client_socket.close()


def handle_client(client_socket, client_address):
    print(f'New client connected: {client_address}')
    clients.append(client_socket)

    username = client_socket.recv(BUFFER_SIZE).decode()
    username_dict[client_socket] = username

    notify_new_client_joined(username, client_socket)

    while True:
        try:
            message = client_socket.recv(BUFFER_SIZE)
            if message:
                broadcast_message(message, client_socket)
            else:
                remove_client(client_socket)
        except:
            remove_client(client_socket)
            break

    print(f'Client disconnected: {client_address}')
    notify_client_disconnected(username)

def notify_new_client_joined(username, sender):
    message = f"{username} joined the chat"
    for client in clients:
        if client != sender:
            client.send(message.encode())

def notify_client_disconnected(username):
    message = f"{username} left the chat"
    for client in clients:
        client.send(message.encode())



SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000
BUFFER_SIZE = 4096

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)

print(f'Server running on socket: {SERVER_PORT}')

clients = []
username_dict = {}

while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.daemon = True
    client_thread.start()


server_socket.close()