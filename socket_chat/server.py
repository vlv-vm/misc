import socket
import threading
import time

SERVER = "localhost"
PORT = 12345
BUFFER = 2048
CLIENTS = list()
ADDRESSES = dict()
BANNED_SOCKETS = list()

srvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srvr.bind((SERVER,PORT))

def broadcast(message, source):
    for client in CLIENTS:
        if client == source:
            pass
        else:
            client.send(message.encode("ASCII"))

def server_broadcast(message):
    for client in CLIENTS:
        client.send(message.encode("ASCII"))

def client_handler(client, nickname):
    #if client in BANNED_SOCKETS:
        #client.send("[*] Banned!".encode("ASCII")))
        #client.close()
    while True:
        try:
            message = f"[{nickname}]: " + client.recv(BUFFER).decode("ASCII")
            broadcast(message, client)
        except ConnectionAbortedError:
            client.close()
        except OSError:
            client.close()
        except:
            client.close()
            ADDRESSES.pop(client)
            CLIENTS.remove(client)
            server_broadcast(f"[*] {nickname} has disconnected!")
            break

def server_admin():
    admin_cmd = "[*] Admin commands:\n[*] /online - lists connected users\n[*] /global 'text' - send message to all users\n[*] /kick 'nickname' - kick user\n[*] /ban 'nickname' - ip ban user\n[*] /banlist - list banned users"
    print(admin_cmd)
    while True:
        command = input(">> ")
        if command.lower() == "/online":
            for user in ADDRESSES:
                print(f"[*] {ADDRESSES[user]}")
        elif command.lower()[0:8] == "/global ":
            server_broadcast(f"[ADMIN]: {command.lower()[8:]}")
        elif command.lower()[0:6] == "/kick ":
            target_user = command[6:]
            try:
                for key in ADDRESSES:
                    if ADDRESSES[key][2] == target_user:
                        key.close()
                        ADDRESSES.pop(key)
                        CLIENTS.remove(key)
            except KeyError:
                print(f"[*] Kicked {target_user}")
        elif command.lower()[0:5] == "/ban ":
            ban_target = command[5:]
            try:
                for soc in ADDRESSES:
                    if ADDRESSES[soc][2] == ban_target:
                        BANNED_SOCKETS.append(soc)
                        
                        ADDRESSES.pop(soc)
                        soc.close()
                        CLIENTS.remove(soc)
            except KeyError:
                print(f"[*] Banned {target_user}")
        elif command.lower()[0:8] == "/banlist":
            for banned_user in BANNED_SOCKETS:
                print(f"[*] {str(banned_user)}")
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
            if client in BANNED_SOCKETS:
                client.send("[*] Banned!".encode("ASCII"))
                client.close()
            client.send("[*] Successfully connected!".encode("ASCII"))
            nickname = client.recv(BUFFER).decode("ASCII")
            print(f"[*] {address[0]}:{address[1]} -> {nickname}")
            joined = f"[*] {nickname} joined the chat!"
            server_broadcast(joined)
            ADDRESSES[client] = [address[0], address[1], nickname]
            CLIENTS.append(client)
            client_handler_thread = threading.Thread(target=client_handler, args=(client,nickname))
            client_handler_thread.start()
        except KeyboardInterrupt:
            srvr.close()
            break
        except:
            print("[*] Error")

start_server()