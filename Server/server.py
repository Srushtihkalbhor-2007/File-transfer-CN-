import socket
import os
import threading

def handle_client(conn, addr):
    print(f"Connected to: {addr}")

    # receive file name
    filename = conn.recv(1024).decode().strip()
    conn.send("ACK".encode())

    # receive file size
    filesize = int(conn.recv(1024).decode().strip())

    if not os.path.exists("received_files"):
        os.makedirs("received_files")

    filepath = os.path.join("received_files", filename)

    file = open(filepath, "wb")

    received = 0

    while received < filesize:
        data = conn.recv(1024)
        if not data:
            break
        file.write(data)
        received += len(data)

        print(f"[{addr}] Receiving... {int((received/filesize)*100)}%")

    file.close()
    conn.close()

    print(f"[{addr}] File received successfully!")


server = socket.socket()
server.bind(("localhost", 5001))
server.listen(5)

print("Server is running and waiting for clients...")

while True:
    conn, addr = server.accept()

    # create new thread for each client
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()