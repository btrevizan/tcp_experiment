from time import time, sleep
from socket import *
import argparse
import os


def main(args):
    global_start = time() * 1000
    buffer_size = 50 * pow(2, 20)
    client = 1

    with socket(AF_INET, SOCK_STREAM) as server_socket:

        server_socket.bind(('', args.port))
        server_socket.listen()

        print('Server active.')

        while True:
            conn, addr = server_socket.accept()
            print('Connected with {}'.format(addr))

            pid = os.fork()

            if pid == 0:  # child
                log_name = 'traffic{}.log'.format(client)

                with conn:
                    total_recv = 0
                    start = int(time() * 1000)

                    while True:
                        data = conn.recv(buffer_size)

                        if data:
                            total_recv = total_recv + len(data)
                        else:
                            print("Connection ended {}".format(addr))
                            exit()

                        stop = int(time() * 1000)
                        if (stop - start) > 1000:  # 1 second
                            x = (stop - global_start) // 1000
                            y = (total_recv * 8) / ((stop - start) / 1000)

                            total_recv = 0
                            start = int(time() * 1000)

                            with open(log_name, 'a') as log:
                                log.write("{},{}\n".format(x, y))

            client = client + 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', dest='port', type=int, required=True, help='Server port.')

    pargs = parser.parse_args()
    main(pargs)

