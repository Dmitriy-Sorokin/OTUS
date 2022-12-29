import socket
import sys

from lesson21_socket.config import LOCALHOST

my_socket = socket.socket()

address_and_port = (LOCALHOST, 8889)

# https://docs.python.org/3/library/socket.html#socket.socket.connect
my_socket.connect(address_and_port)
my_socket.close()
