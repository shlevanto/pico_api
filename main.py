from fastapi import FastAPI

app = FastAPI()

message = ""

@app.get("/")
async def root():
    if message:
        return {"message": message}
    else:
        return {"message": "Pico is offline"}

@app.post("/")
async def receiver(pico_status):
    global message 
    message = pico_status