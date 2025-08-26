import socket

SERVER_HOST = "machinea"   # service name from docker-compose
SERVER_PORT = 9000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

print("🤖 Connected to server! Type 'exit' to quit.")

while True:
    # Client sends message
    msg = input("Client: ")
    client_socket.sendall(msg.encode())

    if msg.lower() == "exit":
        print("❌ Chat ended")
        break

    # Receive reply
    data = client_socket.recv(1024).decode()
    print(f"Server: {data}")

client_socket.close()

