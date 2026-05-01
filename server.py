import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 12345

# List to keep track of connected clients
clients = []
nicknames = []

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                # Remove the client if sending fails
                remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        index = clients.index(client_socket)
        clients.remove(client_socket)
        nickname = nicknames[index]
        nicknames.remove(nickname)
        print(f"{nickname} disconnected")
        broadcast(f"{nickname} left the chat!".encode('utf-8'), client_socket)

def handle_client(client_socket):
    # Receive nickname
    nickname = client_socket.recv(1024).decode('utf-8')
    nicknames.append(nickname)
    clients.append(client_socket)
    print(f"{nickname} joined the chat!")
    broadcast(f"{nickname} joined the chat!".encode('utf-8'), client_socket)

    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
        except:
            break

    remove_client(client_socket)
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr}")
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    main()