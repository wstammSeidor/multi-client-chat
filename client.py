import socket
import threading

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "NICK":
                client.send(nickname.encode("utf-8"))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        message = input()
        if message.startswith("/quit"):
            client.close()
            print("You have disconnected.")
            break
        elif message.startswith("/to-all"):
            content = message[len("/to-all"):].strip()
            client.send(f"[Broadcast] {nickname}: {content}".encode("utf-8"))
        elif message.startswith("/"):
            client.send(message.encode("utf-8"))
        elif message.startswith("/to "):
            client.send(message.encode("utf-8"))
        else:
            client.send(f"{nickname}: {message}".encode("utf-8"))





receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
