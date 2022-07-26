import socket
import time
from concurrent.futures import ThreadPoolExecutor

HOST = "127.0.0.1"  
PORT = 8092

def compute(conn):
    with conn:
        while True:
            data = conn.recv(2000)
            if not data:
                break
            num1, num2 = data.decode('utf-8').split('+')
            data = int(num1) + int(num2)
            data = str(data)
            time.sleep(5)
            conn.sendall(data.encode())
            print(data)          

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    with ThreadPoolExecutor(max_workers = 6) as executor:
        while True:
            conn, addr = s.accept()
            executor.submit(compute, conn)
            