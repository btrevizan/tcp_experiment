from socket import *
import argparse


def main(args):
    with socket(AF_INET, SOCK_STREAM) as server_socket:

        server_socket.bind(('127.0.0.1', args.port))
        server_socket.listen(1)

        print('Server active.')

        while True:
            conn, addr = server_socket.accept()
            print('Connected with {}'.format(addr))

            with conn:
                while True:
                    data = conn.recv(1024)

                    if data:
                        print(data)
                    else:
                        break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', dest='port', type=int, required=True, help='Server port.')

    pargs = parser.parse_args()
    main(pargs)

