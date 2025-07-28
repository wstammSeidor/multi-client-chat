import socket
import threading
import datetime
import random

clients = []
nicknames = []

def load_jokes():
    with open("jokes.txt", "r", encoding="utf-8") as f:
        return f.readlines()

jokes = load_jokes()

def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            client.send(message)

def handle(client):
    while True:
        try:
            msg = client.recv(1024).decode("utf-8")
            response = handle_command(msg, client)
            if response:
                client.send(response.encode("utf-8"))
            else:
                broadcast(msg.encode("utf-8"), sender=client)
        except:
            index = clients.index(client)
            clients.remove(client)
            nickname = nicknames.pop(index)
            broadcast(f"{nickname} has left the chat.".encode("utf-8"))
            client.close()
            break

def handle_command(msg, client):
    if msg.startswith("/help"):
        return "/help, /time, /joke"
    elif msg.startswith("/time"):
        return str(datetime.datetime.now())
    elif msg.startswith("/joke"):
        return random.choice(jokes).strip()
    return None

def receive():
    server.listen()
    print("Server is listening...")
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")
        client.send("NICK".encode("utf-8"))
        nickname = client.recv(1024).decode("utf-8")
        nicknames.append(nickname)
        clients.append(client)
        print(f"Nickname is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode("utf-8"))
        client.send("Connected to the server.".encode("utf-8"))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 55555))

receive()
