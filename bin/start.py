import socket
import time
#import keyboard
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
print('Connecting...')
s.connect(('192.168.3.3', 29999))
time.sleep(0.1)
rcvd = s.recv(4096)
print(rcvd)
print('\n')

def sendCommand(cmd):
    print(cmd)
    cmd = cmd + '\n'
    s.sendall(cmd.encode())
    time.sleep(0.1)
    rcvd = s.recv(4096)
    print(rcvd)
    print('\n')

sendCommand('brake release')
sendCommand('load mj.urp')
time.sleep(7)
sendCommand('play')

while True:
    mylines = []                             # Declare an empty list named mylines.
    with open ('cd.txt', 'rt') as myfile: # Open lorem.txt for reading text data.
        for myline in myfile:                # For each line, stored as myline,
            if myline == 'stop\n':
                sendCommand('stop')
                time.sleep(0.1)
                sendCommand('power off')
                time.sleep(0.2)
                sendCommand('restart safety')
                sys.exit('You stopped the Program!')
            #mylines.append(float(myline))           # add its contents to mylines.
    myfile.close()

# q=1
# while 1:
#     if eval(input())==1:
#         print('You terminated the Program!')
#         sendCommand('stop')
#         sendCommand('power off')
#         break  # finishing the loop
