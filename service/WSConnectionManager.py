from fastapi import WebSocket


class ConnectionManager:
    
    
    def __init__(self) -> None:
        self.connections = {}
        
    async def connect(self,room_id,ws:WebSocket):
        await ws.accept()
        connections = self.connections
        if room_id in connections:
            connections[room_id].append(ws)
        else:
            connections[room_id] = [ws]
            
    async def broadcast(self,room_id,msg):
        connections = self.connections
        for ws in connections[room_id]:
            await ws.send_json(data={
                'message' : str(msg)
            })