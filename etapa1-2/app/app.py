from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def read_root():
    hostname = socket.gethostname()
    return {"hostname": hostname}

@app.get("/health")
def health():
    
    return {"status": "healthy"}