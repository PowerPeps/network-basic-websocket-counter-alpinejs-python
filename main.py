from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

counter = 0
connections = []

@app.get("/")
async def root(): return {"http://127.0.0.1:8000/static/index.html"}

async def broadcast():
    for ws in connections[:]:
        try: await ws.send_text(json.dumps({"counter": counter}))
        except: connections.remove(ws)


@app.websocket("/ws")
async def ws(websocket: WebSocket):
    global counter
    await websocket.accept()
    connections.append(websocket)
    await websocket.send_text(json.dumps({"counter": counter}))
    try:
        while True:
            data = json.loads(await websocket.receive_text())
            if "counter" in data: counter = data["counter"] ; await broadcast()
    except WebSocketDisconnect: connections.remove(websocket)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
