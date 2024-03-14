from fastapi import FastAPI

app = FastAPI()

message = ""

@app.get("/")
async def root():
    return {"message": message}

@app.post("/")
async def receiver(received):
    message = received