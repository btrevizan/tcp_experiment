from time import time, sleep
from socket import *
import argparse


def main(args):
    f = open('traffic.log', 'w').close()
    global_start = time() * 1000
    buffer_size = 50 * pow(2, 20)

    with socket(AF_INET, SOCK_STREAM) as server_socket:

        server_socket.bind(('127.0.0.1', args.port))
        server_socket.listen(2)

        print('Server active.')

        while True:
            conn, addr = server_socket.accept()
            print('Connected with {}'.format(addr))

            with conn:
                total_recv = 0
                start = int(time() * 1000)

                while True:
                    data = conn.recv(buffer_size)

                    if data:
                        total_recv = total_recv + len(data)
                    else:
                        break

                    stop = int(time() * 1000)
                    if (stop - start) > 1000:  # 1 second
                        x = (stop - global_start) // 1000
                        y = (total_recv * 8) / ((stop - start) / 1000)

                        total_recv = 0
                        start = int(time() * 1000)

                        with open('traffic.log', 'a') as log:
                            log.write("{},{}\n".format(x, y))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', dest='port', type=int, required=True, help='Server port.')

    pargs = parser.parse_args()
    main(pargs)

