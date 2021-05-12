import socket
import threading

SRVR = socket.gethostbyname(socket.gethostname())
PORT = 8888

s = socket.socket(socket.AF_INET, socket. SOCK_STREAM)
s.bind((SRVR, PORT))

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def client_handler(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"[DISCONNECT] {nickname} left the chat".encode("ascii"))
            nicknames.remove(nickname)
            break

def start():
    s.listen()
    print(f"[LISTENING] Server is listening on {SRVR}:{PORT}")
    while True:
        client, address = s.accept()
        print(f"[CONNECTED] Connected with {str(address)}")

        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of {address[0]}:{address[1]} is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode("ascii"))
        client.send("[CONNECTED] Connected to the server!".encode("ascii"))

        thread = threading.Thread(target=client_handler, args=(client,))
        thread.start()

start()