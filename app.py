from fastapi import FastAPI
from ws.web_socket_route import ws_route

app = FastAPI()

app.include_router(ws_route,prefix='/ws')