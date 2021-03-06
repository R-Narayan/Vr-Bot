import socket, traceback
import re
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
pwm = GPIO.PWM(7,50)
pwm.start(5)
pwm.ChangeDutyCycle(2)
vals = {
    9:0,
    8:10,
    7:20,
    6:30,
    5:40,
    4:50,
    3:60,
    2:70,
    1:80,
    0:90,
    -1:100,
    -2:110,
    -3:120,
    -4:130,
    -5:140,
    -6:150,
    -7:160,
    -8:170,
    -9:180
}
host = ''
port = 5555
n = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
n.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
n.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
n.bind((host, port))
def cfa(y):
    return y/18 + 2
def servomove(d):
    print(vals[int(float(d))])
    pwm.ChangeDutyCycle(cfa(vals[int(float(d))]))

while 1:
    try:
        message, address = n.recvfrom(8192)
        message = str(message)
        if len(message) > 8:
            message = re.findall(r'[^,\s][^\,]*[^,\s]*',message)
            yeet = re.sub(r'\'','',message[4])
            servomove (yeet)

    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()

