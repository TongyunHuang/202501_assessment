from fastapi import FastAPI, WebSocket

class ConnectionManager:
    def __init__(self):
        self.active_connections = {}

    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        self.active_connections[username] = websocket

    def disconnect(self, username: str):
        del self.active_connections[username]
        
    async def broadcast(self, username: str, message: str):
       for user, user_ws in manager.active_connections.items():
            if user != username:
                await user_ws.send_text(username + ': ' + message)

app = FastAPI()
manager = ConnectionManager()

@app.websocket("/ws/{username}")
async def websocket_endpoint(username: str, websocket: WebSocket):
    await manager.connect(websocket, username)
    print(manager.active_connections)

    try:
        while True:
            message = await websocket.receive_text()
            # Send the received data to the other user
            await manager.broadcast(username, message)
    except:
        # If a user disconnects, remove them from the dictionary
        manager.disconnect(username)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)