import socket
import threading
import os

SERVER = "localhost"
PORT = 12345
BUFFER = 2048

def recieve():
    while True:
        try:
            message = client.recv(BUFFER).decode("ASCII")
            print(message)
        except:
            print("[*] Error, closing connection!")
            client.close()
            break
        
def write():
    while True:
        try:
            message = input("")
            client.send(message.encode("ascii"))
        except:
            print("[*] Error, closing connection!")
            client.close()
            break
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    nickname = input("[*] Enter your nickname: ")
    client.send(nickname.encode("ASCII"))
except:
    print(f"[*] Could not connect, try again later.")
    os.sys.exit()

recv_thread = threading.Thread(target=recieve)
recv_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()