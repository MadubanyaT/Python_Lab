import asyncio
import websockets


async def message(websocket):
    msg = await websocket.recv() # waiting for the message
    print(f"Server Received: {msg}") # displays what the server received

    server_msg = f"Server received this message: \"{msg}\""
    await websocket.send(server_msg) # Sends the message to the client
    print(f"Server Sent: {server_msg}") # Displays the message the server sent

async def main():
    print("Server listening...")
    # Serves the websocket with the message() function, on "localhost", Port 7000
    async with websockets.serve(message, 'localhost', 7000):
        await asyncio.Future() # Always runs and listens. waits for the message then responds to it



if __name__ == "__main__":
    asyncio.run(main())