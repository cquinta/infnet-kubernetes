from fastapi import FastAPI
import socket
import redis

redis = redis.Redis(host='redis', port=6379, db=0)

app = FastAPI()



@app.get("/")
def read_root():
    hostname = socket.gethostname()
    return {"versao":1,"hostname": hostname }
            
@app.get("/req")
def read_req():
    hostname = socket.gethostname()
    redis.incr("key")
    return {"versao":1,"hostname": hostname,"count":redis.get("key")}


@app.get("/health")
def health():
    
    return {"status": "healthy"}

@app.get("/redis")  
async def redis_get():
    return {redis.get("key")}

@app.post("/redis")
async def redis_inc():
    redis.incr("key")