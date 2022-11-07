import fastapi
import uvicorn

print("Hello")
api = fastapi.FastAPI()

@api.get('/')
def index():
    return {"msg": "This is the landing page"}
@api.get('/pai/endpoint')
def endpoint():
    return {"msg": "Hello FastAPI"}

uvicorn.run(api, port=9000)