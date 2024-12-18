from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!! :)"}


@app.get("/about")
async def about():
    return {"version":"v1.0.0",
            "author":"Jorge Abrego",
            "message":"Jorge loves Agupon <3"
            }
    

@app.get("/greet/{name}") 
def greet(name: str): 
    return {"message":f"Hello {name}"}