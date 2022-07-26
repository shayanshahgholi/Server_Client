from concurrent.futures import ThreadPoolExecutor
import socket
import time
from random import randint


def decorators(func):

    def space_lines(*args, **kwargs):
        print("========")
        func(*args, **kwargs)
        print("========")

    return space_lines

def generate_random_number()-> str :
    '''
        This function generates two random numbers and\n
        create a string for send them to server
    '''
    
    random_number1, random_number2 = randint(1, 10), randint(1, 10)
    print(f"generated random numbers:  {random_number1} and {random_number2}")

    out_data = str(str(random_number1) + '+' + str(random_number2))
    print(f"generated string for sending to server: {out_data}")
    
    return out_data
    

@decorators
def run_client(host: str, port: int, buf_size: int = 2**10) -> None:
    '''
        This function generates two random numbers and send\n
        them as "<first random number>+<second random number>" to server.\n

        Then prints the server response.
    '''

    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_.connect((host, port))

    out_data = generate_random_number()
    socket_.sendall(bytes(out_data, 'UTF-8'))

    response = socket_.recv(buf_size)
    response = response.decode()
    print(f"server response: {response}")

    socket_.close()


if __name__ == '__main__':
    SPACE_LINES_FOR_TERMINAL = True

    SERVER = "127.0.0.1"
    PORT = 8092
    NUMBER_OF_REQUESTS = 10

    executer = ThreadPoolExecutor(NUMBER_OF_REQUESTS)

    for _ in range(NUMBER_OF_REQUESTS):
        executer.submit(run_client, SERVER, PORT)
        time.sleep(1)

