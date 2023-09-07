#In here i thing we have to put or own code
#  print("Hello World")
import os
import subprocess
import sys
import socket 

#ip = raw_input("enter the IP Address: ")
p#ort = input("Enter the Port Number: ")

hostname = "192.168.64.129"
port     = 5555
#BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
# separator string for sending 2 messages in one go
#SEPARATOR = "<sep>"


def run((host, port)):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.run((host, port))

run(hostname. port)
