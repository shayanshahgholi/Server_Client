from socket import AF_INET, SOCK_STREAM, socket
from time import sleep
from concurrent.futures import ThreadPoolExecutor


def compute(conn: socket, buffer_size=2**10) -> None:
    '''
        This function handles the connections from clients.\n

        Example:\n 
            <-- [client] 4+6
            --> [server] 10


        :param conn: tcp socket
    '''

    while True:
        data = conn.recv(buffer_size)
        if not data:
            break

        num1, num2 = data.decode('utf-8').split('+')
        response = int(num1) + int(num2)

        sleep(5)

        conn.sendall(str(response).encode())
        print(f"data: {data.decode()}  -->  num1: {num1}  and  num2: {num2}  -->  response: {response}")


def turn_server_on(host: str, port: int) -> socket:
    '''
        This function binds server on given host and port.\n
        And then, starts listening on socket.

        See Also:
            socket.bind()\n
            socket.listen()


        :param host: ip address to bind server
        :param port: port number to bind server

        :return: opened tcp socket
    '''
    socket_ = socket(AF_INET, SOCK_STREAM)
    socket_.bind((host, port))
    socket_.listen()

    return socket_


def server_handler(socket_: socket, max_workers: int=6)-> None:
    '''
        This function handles max_workers of connections on given socket.

        :param socket_: binded tcp socket
        :param max_workers: maximum number of connections to handle
    '''

    with ThreadPoolExecutor(max_workers) as executor:
        while True:
            conn = socket_.accept()[0]
            executor.submit(compute, conn)


if __name__ == '__main__':
    HOST = "127.0.0.1"
    PORT = 8092
    socket_ = turn_server_on(HOST, PORT)
    server_handler(socket_)
