from guizero import App, PushButton, TextBox, Text, Box
#import subprocess
import time
import sys

##Popen(['python3', 'sync.py'])

step = float(100)
yaw = float(-1690)
pitch = float(1.75)
roll = float(-1.585)

mylines = []                             # Declare an empty list named mylines.
with open ('cd.txt', 'rt') as myfile: # Open lorem.txt for reading text data.
    for myline in myfile:                # For each line, stored as myline,
        if myline == 'stop\n':
            sys.exit('Unexpected Stop detected!!!')
        mylines.append(float(myline))           # add its contents to mylines.
myfile.close()

yaw = float(mylines[0])
##dy = mylines[1]/1000
##dz = mylines[2]/1000
roll = float(mylines[3])
pitch = float(mylines[4])
##yaw = mylines[5]

i = False
def play():
    global i
    if i == False:
        if len(mylines) != 6 or roll != 1.56:
            reference()
            write()
##        subprocess.Popen(['start','sync.py'])
##        subprocess.Popen(['start','start.py'])
        time.sleep(5)
        i = True
        button.text = "Stop"
    else:
        with open("cd.txt", "w") as f:
            f.write(str(yaw)+"\n")
            f.write(str(0.0)+"\n")
            f.write(str(0.0)+"\n")
            f.write(str(roll)+"\n")
            f.write(str(pitch)+"\n")
            f.write("stop"+"\n")
        f.close()
        time.sleep(3)
        write()
        i = False
        time.sleep(1)
        button.text = "Reboot"

def reference():
    global yaw
    global pitch
    global roll
    yaw = float(-1600)
    pitch = float(1.45)
    roll = float(1.56)

def exit_app():
    if i == True:
        if app.yesno("Warning!", "Exit without pwering ur10 off?"):
            app.destroy()
        else:
            play()
    else:
        if app.yesno("Options...", "Fallback to reference pose when started next time?"):
            reference()
            write()
            app.destroy()
        else:
            app.destroy()

def step_length():
    global step
    step = float(step_box.value)
    message.value = "yaw="+str(yaw)+", "+"pitch="+str(pitch)
    
def write():
    with open("cd.txt", "w") as f:
        f.write(str(yaw)+"\n")
        f.write(str(0.0)+"\n")
        f.write(str(0.0)+"\n")
        f.write(str(roll)+"\n")
        f.write(str(pitch)+"\n")
        f.write(str(0.0)+"\n")
    f.close()
    message.value = "yaw="+str(yaw)+", "+"pitch="+str(pitch)

def left():
    global yaw
    yaw = yaw + step
    write()
    app.title = "yaw left"
    #message.value = "yaw="+str(yaw)+", "+"pitch="+str(pitch)

def right():
    global yaw
    yaw = yaw - step
    write()
    app.title = "yaw right"
    #message.value = "yaw="+str(yaw)+", "+"pitch="+str(pitch)

def up():
    global pitch
    pitch = pitch + step/1000
    write()
    app.title = "pitch up"
    #message.value = "yaw="+str(yaw)+", "+"pitch="+str(pitch)

def down():
    global pitch
    pitch = pitch - step/1000
    write()
    app.title = "pitch down"
    #message.value = "yaw="+str(yaw)+", "+"pitch="+str(pitch)

app = App(title="ui.py", width=620, height=700)

control_box = Box(app, align="top", height=100, width="fill", border=True)
button = PushButton(control_box, width=10, height=5, align="left", text="Start", command=play)
step_box = TextBox(control_box, align="left", width=5, text=str(step), command=step_length)
step_box.text_size=28
message = Text(control_box, align="right", text="yaw="+str(yaw)+", "+"pitch="+str(pitch))
message.text_size=20

button_box = Box(app, align="bottom", width="fill", height="fill", border=True)
##close_button = PushButton(button_box, grid=[1,1], text="Exit", command=exit_app)
left_button = PushButton(button_box, width=20, height=10, align="left", text="Left", command=left)
right_button = PushButton(button_box, width=20, height=10, align="right", text="Right", command=right)
up_button = PushButton(button_box, width=20, height=10, align="top", text="Up", command=up)
down_button = PushButton(button_box, width=20, height=10, align="bottom", text="Down", command=down)

app.when_closed = exit_app

app.display()
