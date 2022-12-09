import socket
import asyncio
from websockets import serve
import RPi.GPIO as GPIO
from time import sleep





def low():
    GPIO.output(21, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)

def down():
    GPIO.output(21, GPIO.LOW)
    GPIO.output(20, GPIO.HIGH)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(26, GPIO.HIGH)

def up():
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(19, GPIO.HIGH)

def left():
    GPIO.output(21, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(26, GPIO.HIGH)

def right():
    GPIO.output(21, GPIO.LOW)
    GPIO.output(20, GPIO.HIGH)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)

def rangle_left():
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(26, GPIO.HIGH)

def rangle_right():
    GPIO.output(21, GPIO.LOW)
    GPIO.output(20, GPIO.HIGH)
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(26, GPIO.LOW)


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('google.com', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)

async def echo(websocket):
    async for message in websocket:
        
        data = message
        await websocket.send(message)
        try:
            if(data == "left"):
                left()

            elif(data == "right"):
                right()

            elif(data == "up"):
                up()

            elif(data == "down"):
                down()

            elif(data == "rangle_right"):
                rangle_right()
            
            elif(data == "rangle_left"):
                rangle_left()
           
            elif(data == "low"):
                low()

        except KeyboardInterrupt:
            GPIO.cleanup()
            setup()
        # GPIO.cleanup()
        
setup()
async def main():
    async with serve(echo, get_ip(), 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())