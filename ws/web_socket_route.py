from fastapi import WebSocket,APIRouter
from service.WSConnectionManager import ConnectionManager
ws_route = APIRouter(prefix='/wsroute')

manager = ConnectionManager()

@ws_route.websocket('/{room}/connect')
async def web_socket_connection(room,websocket:WebSocket):
    await manager.connect(room,websocket)
    while True:
        data = await websocket.receive_json()
        await manager.broadcast(room,data['message'])
    
    
    