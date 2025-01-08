app = FastAPI()
class ConnectionManager:
    def __init__(self):
        pass

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        pass

    def disconnect(self, websocket: WebSocket):
        pass

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            pass

manager = ConnectionManager()

@app.websocket("/ws/{username}")

async def websocket_endpoint(websocket: WebSocket, username: str):
    pass