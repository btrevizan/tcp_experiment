from time import sleep
from socket import *
import argparse


def main(args):
    with socket(AF_INET, SOCK_STREAM) as client_socket:

        addr = (args.addr, args.port)
        client_socket.connect(addr)
        print('Connected with {}'.format(addr))

        while True:
            client_socket.send(b'Dummy' * 250)  # sending 1250 bytes


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--addr', dest='addr', type=str, required=True, help='Server IP address.')
    parser.add_argument('-p', '--port', dest='port', type=int, required=True, help='Server port.')

    pargs = parser.parse_args()
    main(pargs)

