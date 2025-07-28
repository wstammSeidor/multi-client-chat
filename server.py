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
            print(f"{nickname} has disconnected.")
            client.close()
            break


def handle_command(msg, client):
    if msg.startswith("/help"):
        return "/help, /time, /joke /to-all <message>, /users, /quit"
    elif msg.startswith("/time"):
        return str(datetime.datetime.now())
    elif msg.startswith("/joke"):
        return random.choice(jokes).strip()
    elif msg.startswith("/users"):
        return "Connected users: " + ", ".join(nicknames)
    elif msg.startswith("/to "):
        parts = msg.split(" ", 2)  # /to user2 mensaje
        if len(parts) < 3:
            return "Usage: /to <username> <message>"
        
        target_name = parts[1]
        content = parts[2]
        
        if target_name in nicknames:
            target_index = nicknames.index(target_name)
            sender_index = clients.index(client)
            sender_name = nicknames[sender_index]
            clients[target_index].send(f"[Private] {sender_name}: {content}".encode("utf-8"))
            return f"[Private to {target_name}]: {content}"  # Eco para quien lo envió
        else:
            return f"User '{target_name}' not found."
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
        
        # Anunciar a todos los demás que llegó uno nuevo
        broadcast(f"{nickname} joined the chat!".encode("utf-8"), sender=client)

        # Confirmación al nuevo cliente
        client.send("Connected to the server.".encode("utf-8"))

        # Enviar la lista de usuarios conectados (excepto él mismo)
        if len(nicknames) > 1:
            other_users = ", ".join(nicknames[:-1])
            client.send(f"Users already in the chat: {other_users}".encode("utf-8"))

        # Crear nuevo hilo para escuchar mensajes de este cliente
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 55555))

receive()
