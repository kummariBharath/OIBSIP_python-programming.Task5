# Basic Text-Based Chat Application

A simple real-time chat application in Python using a client-server model. Users can exchange messages via the command line in real-time.

## Features
- Real-time message broadcasting to all connected clients.
- Multi-client support using threading.
- Command-line interface for sending and receiving messages.
- Simple nickname-based identification.

## Code Explanation

### Server (`server.py`)
The server handles client connections and message broadcasting.

- **Configuration**: Listens on `127.0.0.1:12345`.
- **Client Management**: Maintains lists of connected clients and their nicknames.
- **Functions**:
  - `broadcast(message, client_socket)`: Sends a message to all clients except the sender.
  - `remove_client(client_socket)`: Removes a disconnected client and notifies others.
  - `handle_client(client_socket)`: Handles incoming messages from a client and broadcasts them.
- **Main Loop**: Accepts new connections and starts a thread for each client.

### Client (`client.py`)
The client connects to the server and facilitates message exchange.

- **Configuration**: Connects to `127.0.0.1:12345`.
- **Functions**:
  - `receive_messages(client_socket)`: Runs in a thread to continuously receive and print messages.
  - `send_messages(client_socket, nickname)`: Runs in a thread to read user input and send messages.
- **Main Flow**: Prompts for nickname, connects to server, and starts send/receive threads.

## Execution Steps

1. **Start the Server**:
   - Open a terminal (PowerShell or Command Prompt).
   - Navigate to the project directory: `cd "D:\OIBSIP_python programming.Task5"`
   - Activate the virtual environment:  
     ```
     .venv\Scripts\Activate.ps1
     ```
   - Run the server:  
     ```
     python server.py
     ```
     You should see: `Server listening on 127.0.0.1:12345`

2. **Start the First Client**:
   - Open a **new terminal** window.
   - Navigate to the project directory: `cd "D:\OIBSIP_python programming.Task5"`
   - Activate the virtual environment:  
     ```
     .venv\Scripts\Activate.ps1
     ```
   - Run the client:  
     ```
     python client.py
     ```
   - Enter a nickname when prompted (e.g., `Alice`).
   - You should see a message like `Alice joined the chat!` in the server terminal.

3. **Start the Second Client** (for chatting):
   - Open **another new terminal** window.
   - Repeat the steps for the first client, but enter a different nickname (e.g., `Bob`).
   - Now both clients are connected.

4. **Chat**:
   - In each client terminal, type messages and press Enter to send.
   - Messages will appear in real-time in the other client's terminal.
   - To exit, close the terminal or use Ctrl+C (this will disconnect the client).

### Notes
- The server must be running before starting clients.
- Each client runs in its own terminal for simultaneous input/output.
- If you encounter issues, ensure the virtual environment is activated and Python is available.
- The server handles multiple clients, so you can add more by repeating step 2-3.