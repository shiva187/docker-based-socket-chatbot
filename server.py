import socket

HOST = "0.0.0.0"
PORT = 9000

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("🤖 Server is waiting for connection...")

conn, addr = server_socket.accept()
print(f"✅ Connected by {addr}")

while True:
    # Receive message
    data = conn.recv(1024).decode()
    if not data or data.lower() == "exit":
        print("❌ Client ended chat")
        break

    print(f"Client: {data}")

    # Server reply (chatbot-style)
    reply = input("Server: ")  # you type the reply
    conn.sendall(reply.encode())

conn.close()

