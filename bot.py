#In here i thing we have to put or own code
#  print("Hello World")
import os
import subprocess
import sys

hostname = sys.argv[1]
port = int(sys.argv[2])
#BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
# separator string for sending 2 messages in one go
#SEPARATOR = "<sep>"


def run(hn, p):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect((hn, p))

run(hostname. port)
