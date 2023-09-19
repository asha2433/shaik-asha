import socket
import json
import sys

def send_message(sock, message):
    try:
        sock.send(message.encode())
    except Exception as e:
        print(f"Error sending message: {str(e)}")
        sys.exit(1)

def main():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    server1_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server1_socket.connect((config['server1_ip'], config['server1_port']))

    server2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server2_socket.connect((config['server2_ip'], config['server2_port']))

    try:
        while True:
            message = input("Send message to servers: ")
            send_message(server1_socket, message)
            send_message(server2_socket, message)

            if message.lower() == 'exit':
                break

    except KeyboardInterrupt:
        pass  # Handle keyboard interrupt gracefully

    finally:
        send_message(server1_socket, "client exit from chatting")
        send_message(server2_socket, "client exit from chatting")
        server1_socket.close()
        server2_socket.close()

if __name__ == '__main__':
    main()


























