import socket
import json

def main():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((config['server1_ip'], config['server1_port']))
    server_socket.listen(5)
    print("Server 1 listening...")

    client_socket, _ = server_socket.accept()
    print("Connected to client")

    try:
        while True:
            message = client_socket.recv(config['buffer_size']).decode()
            if not message:
                break
            print(f"Received msg from client: {message}")
    except KeyboardInterrupt:
        pass  # Handle keyboard interrupt gracefully
    finally:
        client_socket.close()
        server_socket.close()

if __name__ == '__main__':
    main()
