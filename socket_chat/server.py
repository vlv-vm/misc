import socket
import threading
import time

SERVER = "localhost"
PORT = 12345
BUFFER = 2048
CLIENTS = list()
BANNED_SOCKETS = list()

srvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srvr.bind((SERVER,PORT))

def broadcast(message, source):
    for client in CLIENTS:
        if client[0] == source:
            pass
        else:
            client[0].send(f"[{time.strftime('%H:%M',time.localtime())}] {message}".encode('ASCII'))

def server_broadcast(message):
    for client in CLIENTS:
        client[0].send(message.encode("ASCII"))

def client_handler(client, ip, port, nickname):
    while True:
        try:
            message = f"{nickname}: {client.recv(BUFFER).decode('ASCII')}"
            broadcast(message, client)
        except ConnectionAbortedError:
            client.close()
        except OSError:
            client.close()
        except:
            CLIENTS.remove([client, ip, port, nickname])
            client.close()
            server_broadcast(f"[*] {nickname} has disconnected!")
            break

def server_admin():
    admin_cmd = "[*] Admin commands:\n[*] /online - lists connected users\n[*] /global 'text' - send message to all users\n[*] /kick 'nickname' - kick user\n[*] /ban 'nickname' - ip ban user\n[*] /banlist - list banned users"
    print(admin_cmd)
    while True:
        command = input(">> ")
        if command.lower() == "/online":
            for user in CLIENTS:
                print(f"[*] {user[1]}:{user[2]} {user[3]}")
        elif command.lower()[0:8] == "/global ":
            server_broadcast(f"[ADMIN]: {command.lower()[8:]}")
        elif command.lower()[0:6] == "/kick ":
            target_user = command[6:]
            try:
                for client in CLIENTS:
                    if client[3] == target_user:
                        BANNED_SOCKETS.append(client[0])
                        client[0].close()
                        CLIENTS.remove(client)
            except KeyError:
                print(f"[*] Kicked {target_user}")
        elif command.lower()[0:5] == "/ban ":
            ban_target = command[5:]
            try:
                for ban_client in CLIENTS:
                    if ban_client[3] == ban_target:
                        BANNED_SOCKETS.append([ban_client[1], ban_client[2]])
                        CLIENTS.remove(ban_client)
                        ban_client[0].close()
            except KeyError:
                print(f"[*] Banned {target_user}")
        elif command.lower()[0:8] == "/banlist":
            for banned_client in BANNED_SOCKETS:
                print(f"[*] {str(banned_client)}")
        else:
            print(admin_cmd)

def start_server():
    srvr.listen()
    print(f"[*] Listening on {SERVER}:{PORT}")
    admin_thread = threading.Thread(target=server_admin)
    admin_thread.start()
    while True:
        try:
            client, address = srvr.accept()
            print(f"[*] {address[0]}:{address[1]} has connected")
            ban_check = [address[0], address[1]]
            if ban_check in BANNED_SOCKETS:
                client.send("[*] Banned!".encode("ASCII"))
                client.close()
            client.send("[*] Successfully connected!".encode("ASCII"))
            nickname = client.recv(BUFFER).decode("ASCII")
            print(f"[*] {address[0]}:{address[1]} -> {nickname}")
            joined = f"[*] {nickname} joined the chat!"
            server_broadcast(joined)
            CLIENTS.append([client, address[0], address[1], nickname])
            client_handler_thread = threading.Thread(target=client_handler, args=(client,address[0],address[1],nickname))
            client_handler_thread.start()
        except KeyboardInterrupt:
            srvr.close()
            break
        except:
            print("[*] Error")

start_server()
