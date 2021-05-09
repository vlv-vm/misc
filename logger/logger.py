import socket
import threading

server = socket.gethostbyname(socket.gethostname())
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))

s.listen()
print(f"LISTENING on {server}:{port}")

#while True:
client, address = s.accept()
client_req = client.recv(2048).decode('ASCII')
print(f"CLIENT: {client}\nIP: {address[0]}\nPORT: {address[1]}\nREQUEST: {client_req}")

req = client_req.split()
print(f"\n\n\n{req}")
    
method, path, protocol = req[0], req[1], req[2]
print(f"\n\n\nMETHOD: {method}\nPATH: {path}\nPROTOCOL: {protocol}")

client.close()