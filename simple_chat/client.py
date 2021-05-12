import threading
import socket

nickname = input("Enter your nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.75.1", 8888))

def recieve():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "NICK":
                client.send(nickname.encode("ascii"))
            else:
                print(message)
        except:
            print("[ERROR] An error occurred!")
            client.close()
            break

def write():
    while True:
        message = f"{nickname:}: {input('')}"
        client.send(message.encode("ascii"))

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()