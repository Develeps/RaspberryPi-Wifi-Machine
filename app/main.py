import asyncio
from websockets import connect
import keyboard
import time

async def hello(uri):
    async with connect(uri) as websocket:
        while True:
            if keyboard.is_pressed("w"):
                await websocket.send("up")
                
            elif keyboard.is_pressed("s"):
                await websocket.send("down")
            
            elif keyboard.is_pressed("d"):
                await websocket.send("right")
            
            elif keyboard.is_pressed("a"):
                await websocket.send("left")
            
            elif keyboard.is_pressed("q"):
                await websocket.send("rangle_left")
            
            elif keyboard.is_pressed("e"):
                await websocket.send("rangle_right")
            
            else:
                await websocket.send("low")

            time.sleep(0.1)
            await websocket.recv()
            # print(data)

ip = input("Введите IP: ")            

asyncio.run(hello(f"ws://{ip}:8765"))