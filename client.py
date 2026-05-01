import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 12345

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Connection lost.")
            client_socket.close()
            break

def send_messages(client_socket, nickname):
    while True:
        message = input()
        full_message = f"{nickname}: {message}"
        client_socket.send(full_message.encode('utf-8'))

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    nickname = input("Enter your nickname: ")
    client.send(nickname.encode('utf-8'))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client, nickname))
    send_thread.start()

if __name__ == "__main__":
    main()