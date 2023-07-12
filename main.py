import socket
import threading
from queue import Queue
import time

target = "192.168.1.2"
queue = Queue()
open_port = []

def prot_scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

def fillQueue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if prot_scan(port):
            print(f"Open {port}")
            open_port.append(port)
        time.sleep(0.01)

port_list = []
for prot in range(1,9000):
    port_list.append(prot)
    time.sleep(0.01)
fillQueue(port_list)

thread_list = []

for _ in range(500):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)
    time.sleep(0.01)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports:", open_port)
