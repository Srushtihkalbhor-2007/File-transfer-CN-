import socket
import os
import time

client = socket.socket()
client.connect(("localhost", 5001))

filename = "send.txt"
filesize = os.path.getsize(filename)
filename = "text.txt"
filesize = os.path.getsize(filename)

# send filename
client.send(filename.encode())
client.recv(1024)

time.sleep(0.1)  # 👈 ADD THIS

# send filesize
client.send(str(filesize).encode())

time.sleep(0.1)  # 👈 ADD THIS

# open file
file = open(filename, "rb")

sent = 0

while True:
    data = file.read(1024)
    if not data:
        break
    client.send(data)
    sent += len(data)

    print(f"Sending... {int((sent/filesize)*100)}%")

file.close()
client.close()

print("File sent successfully!")