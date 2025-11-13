from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

counter = 0

class CounterUpdate(BaseModel):
    counter: int

@app.get("/api/counter")
async def get_counter():
    return JSONResponse({"counter": counter})

@app.post("/api/counter")
async def update_counter(data: CounterUpdate):
    global counter
    counter = data.counter
    return JSONResponse({"counter": counter})

app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
