import asyncio
import websockets

async def client_message():
    uri = 'ws://localhost:7000'
    async with websockets.connect(uri) as websocket: # Connects to the server websocket
        msg = input("Enter your message to the server: ") # Client input

        await websocket.send(msg)  # Sending the message to the server
        print(f'Client Sent: {msg}')

        server_response = await websocket.recv() # Receiving response from the server
        print(f"The server's response: {server_response}")

if __name__ == "__main__":
    asyncio.run(client_message())



