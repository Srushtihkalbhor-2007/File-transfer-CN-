import socket
import os
import tkinter as tk
from tkinter import filedialog, ttk

selected_file = ""

def choose_file():
    global selected_file
    selected_file = filedialog.askopenfilename()
    
    if selected_file:
        file_label.config(text=os.path.basename(selected_file))

def send_file():
    if not selected_file:
        status_label.config(text="Select a file first!")
        return

    try:
        status_label.config(text="Connecting...")
        root.update()

        client = socket.socket()
        client.connect(("localhost", 5001))

        filename = os.path.basename(selected_file)
        filesize = os.path.getsize(selected_file)

        client.send(filename.encode())
        client.recv(1024)
        client.send(str(filesize).encode())

        file = open(selected_file, "rb")

        sent = 0
        progress['value'] = 0

        status_label.config(text="Sending...")

        while True:
            data = file.read(1024)
            if not data:
                break
            client.send(data)
            sent += len(data)

            percent = int((sent/filesize)*100)
            progress['value'] = percent
            root.update()

        file.close()
        client.close()

        status_label.config(text="File sent successfully!")

    except Exception as e:
        status_label.config(text=f"Error: {e}")


# GUI
root = tk.Tk()
root.title("File Transfer Client")
root.geometry("350x250")

tk.Label(root, text="File Transfer Client", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Select File", command=choose_file).pack(pady=5)

file_label = tk.Label(root, text="No file selected")
file_label.pack()

tk.Button(root, text="Send File", command=send_file).pack(pady=10)

progress = ttk.Progressbar(root, orient="horizontal", length=250, mode="determinate")
progress.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()