import socket
import threading
import json

with open('config.json') as config_file:
    config = json.load(config_file)
    host = config['server_address']
    port = config['port']


def handle_client(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received from {client_address}: {message}")
        except Exception as e:
            print(f"Error handling client {client_address}: {e}")
            break
    clients.remove(client_socket)
    client_socket.close()


def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode('utf-8'))
        except:
            continue


def send_messages():
    while True:
        message = input("Server: ")
        formatted_message = f"Server: {message}"
        broadcast(formatted_message, client_socket)


# host = '0.0.0.0' # Listen on all available interfaces
# port = 8082


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

clients = []

print(f"Server listening on {host}:{port}")

send_thread = threading.Thread(target=send_messages)
send_thread.start()

while True:
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address}")
    clients.append(client_socket)
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()

