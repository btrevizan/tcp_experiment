# TCP Experiment
Small experiment about TCP congestion control and fairness written in Python.

## Running server.py
Usage:
```
usage: server.py [-h] -p PORT

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Server port.
```

Example:
```bash
$ python3 server.py -p 4003
```

## Running client.py
Usage:
```
usage: client.py [-h] -a ADDR -p PORT

optional arguments:
  -h, --help            show this help message and exit
  -a ADDR, --addr ADDR  Server IP address.
  -p PORT, --port PORT  Server port.
```

Example:
```bash
$ python3 client.py -a 127.0.0.1 -p 4003
```

## Graphic log
To run a graphic representation of log files generated, just run:
```bash
$ python3 traffic.py
```