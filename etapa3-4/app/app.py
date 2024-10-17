from fastapi import FastAPI
import socket
import redis

redis = redis.Redis(host='redis', port=6379, db=0)

app = FastAPI()



@app.get("/")
def read_root():
    hostname = socket.gethostname()
    redis.incr("key")
    return {"hostname": hostname, "counter": redis.get("key")}

@app.get("/health")
def health():
    
    return {"status": "healthy"}

@app.get("/redis")  
async def redis_get():
    return {redis.get("key")}

@app.post("/redis")
async def redis_inc():
    redis.incr("key")