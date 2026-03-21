# File Transfer Project (CN)

A client-server application for transferring files and folders between systems over a network.

# Features

- Transfer files and folders between client and server
- User-friendly GUI interface
- Command-line interface option
- Real-time transfer status
- Cross-platform compatibility

# Prerequisites

- Python 3.6 or higher installed on both client and server machines
- Network connectivity between client and server (LAN or same network)
- Required Python libraries: `tkinter` (usually comes with Python), `socket` (built-in)

# Project Structure
Client/
├── client.py # Client core functionality
├── client_gui.py # Client GUI interface
├── send.txt # Files to send configuration
└── text.txt # Sample text file

Server/
├── server.py # Server core functionality
├── README.md # Documentation
└── received.txt # Received files log

# How to Run

1. Start the Server
On the server machine:
cd Server
python server.py
The server will start listening for incoming connections. You should see:
Server started on 0.0.0.0:5000
Waiting for connections...


2. Start the Client
On the client machine:
cd Client
python client_gui.py
Or use command line version:

cd Client
python client.py

3. Transfer Files
Using GUI (client_gui.py):
In the GUI window:

Enter the server's IP address (e.g., 192.168.1.100)
Enter the port number (default: 5000)
Click "Select Files" to choose individual files, or
Click "Select Folder" to choose an entire folder
Click "Send" to start the transfer

4. Verify Transfer
On the server side, you'll see transfer progress and confirmation
Received files will appear in the Server/ directory
Check received.txt for transfer logs

# Configuration
Server Configuration
Port: Modify in server.py (default: 5000)
Save Location: Files are saved in the Server directory
Client Configuration
Server IP: Update in client files or enter at runtime
Port: Must match server port (default: 5000)
send.txt: List files to transfer (one per line)

# Network Setup
To find your server's IP address:
Windows: ipconfig (look for IPv4 Address)
Linux/Mac: ifconfig or ip addr
Note: Both client and server must be on the same network or have proper port forwarding configured.

# Troubleshooting
Connection Refused Error
Ensure server is running before starting client
Check firewall settings (allow port 5000)
Verify server IP address is correct
Confirm both devices are on the same network
Try using localhost (127.0.0.1) for testing on same machine

# Files Not Transferring
Check file permissions
Verify file paths are correct
Ensure sufficient disk space on server
Check if files are open/locked by another program

# Port Already in Use
Change the port number in both client and server
Or kill the process using the port:

# Testing on Single Machine
For testing both client and server on the same computer:
Open two terminal windows
In terminal 1, start the server:
cd Server
python server.py
In terminal 2, start the client:
cd Client
python client_gui.py
Use 127.0.0.1 or localhost as the server IP


# Notes
All received files are saved in the Server/ directory
Transfer logs are stored in received.txt
The server can handle multiple transfers sequentially
Large files may take time depending on network speed
Make sure both systems are on the same network (or VPN)
Transfer logs are stored in received.txt

Make sure both systems are on the same network
