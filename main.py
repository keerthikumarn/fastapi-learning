from fastapi import FastAPI

#create FastAPI instance
app = FastAPI()

# a simple GET API end point
@app.get("/hello")
def print_hello():
    return {"message": "welcome the world of FastAPI programming!"}
