import socket
import threading
import json

with open('config.json') as config_file:
    config = json.load(config_file)
    host = config['server_address']
    port = config['port']


def receive_messages(client_socket):
    while True:
        try:
            # if client_socket != message:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Disconnected from server.")
            break


# host = '127.0.0.1' # Replace with the server's IP address
# port = 1283


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

print(f"Connected to server at {host}:{port}")

receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

while True:
    message = input("You:")
    client.send(message.encode('utf-8'))
client.close()
