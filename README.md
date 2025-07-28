# Overview

This project is a multi-client chat application developed in Python using the socket and threading libraries. The purpose of this software is to deepen my understanding of network communication by implementing a real-time client-server system that supports concurrent connections and custom commands.

The application uses the client-server model. The server accepts multiple connections from different clients, and each client can send messages or commands. The server either responds to those commands or broadcasts messages to all other connected clients.

To run the program:
- Start the server by running `python server.py`
- Then start one or more clients using `python client.py`
- Each client must enter a nickname when prompted
- Clients can send messages or special commands like `/help`, `/time`, and `/joke`

This software was created to explore how real-time communication can be handled over a TCP network, and to practice multithreading, socket programming, and command handling in Python.

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

The project uses the **Client/Server** architecture.

The protocol used is **TCP**, and communication occurs through **port 55555** on `127.0.0.1` (localhost).

Messages follow a simple text-based format:
- Commands like `/help`, `/time`, or `/joke` are sent as plain strings.
- Regular messages are sent as `nickname: message`.
- The server parses messages and distinguishes between commands and general chat messages.

# Development Environment

The software was developed using the following tools:

- **Visual Studio Code** as the main code editor
- **Python 3.10** as the programming language
- No external libraries were required — only the Python standard library:
  - `socket` for TCP communication
  - `threading` for handling multiple clients concurrently
  - `datetime` for timestamps
  - `random` for selecting jokes
  - `os` (optional) for file operations if needed

# Useful Websites

* [Python Socket Programming](https://realpython.com/python-sockets/)
* [Python Threading](https://docs.python.org/3/library/threading.html)
* [Python socket — official docs](https://docs.python.org/3/library/socket.html)
* [Client-Server Architecture (Wikipedia)](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)
* [OSI Model Overview](https://en.wikipedia.org/wiki/OSI_model)

# Future Work

* Add a GUI using `tkinter` for a better user experience
* Encrypt messages for secure communication
* Add a command to list online users
* Improve error handling and connection recovery
* Allow clients to change nicknames mid-session
