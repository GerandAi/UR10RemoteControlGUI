import socket
import time
#import keyboard

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
print('Connecting...')
s.connect(('192.168.3.3', 29999))
time.sleep(0.01)
rcvd = s.recv(4096)
print(rcvd)
print('\n')

def sendCommand(cmd):
    print(cmd)
    cmd = cmd + '\n'
    s.sendall(cmd.encode())
    time.sleep(0.01)
    rcvd = s.recv(4096)
    print(rcvd)
    print('\n')

while True:
    cmd = input("Enter a command: ")
    if cmd=='exit' :
        cmd = 'quit'
        sendCommand(cmd)
        print('Exiting...')
        time.sleep(1)
        break
    else :
        sendCommand(cmd)
