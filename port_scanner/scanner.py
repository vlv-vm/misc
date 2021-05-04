import socket
import threading
import time
import sys

vulnports = [21,22,23,25,53,80,88,443]
open_ports = []
threads = []

host = input("IP: ")

def vulnports_thread(vulnports):
    for i in vulnports:
        t = threading.Thread(target = port_scanner, args = [i])
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

def port_scanner(i):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    try:
        connection = s.connect((host,i))
        print("OPEN   " + str(i))
        open_ports.append(i)
        s.close()
    except:
        print("closed " + str(i))

def range_thread(a, b):
    for i in range(a, b):
        t = threading.Thread(target = port_scanner, args = [i])
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

def main(a, b):
    start = time.perf_counter()
    range_thread(a, b)
    finish = time.perf_counter()
    print("Finished in " + str(finish - start) + " seconds")
    print("Open ports:")
    for i in open_ports:
        sys.stdout.write(str(i) + " ")

while True:
    print("Option 1 Port 0 - 1023\nOption 2 Port 1024 - 49151\nOption 3 Port 49152 - 65535\nOption 4 Vulnerable Ports\nOption 5 All ports")
    option = int(input("Enter 1, 2, 3, 4, 5: "))
    if option == 1 or option == 2 or option == 3 or option == 4 or option == 5:
        break

if option == 1:
    main(0, 1025)
elif option == 2:
    main(1025, 49152)
elif option == 3:
    main(49152, 65536)
elif option == 4:
    start = time.perf_counter()
    vulnports_thread(vulnports)
    finish = time.perf_counter()
    print("Finished in " + str(finish - start) + " seconds")
    print("Open ports:")
    for i in open_ports:
        sys.stdout.write(str(i) + " ")
else:
    main(0, 65536)
    
