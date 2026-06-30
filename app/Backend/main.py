from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "welcome to travel agent"
    }
@app.get("/about")
def about():
    return {
        "message": "this is a travel agent app"
    }
@app.get("/trips")
def trips():
    return {
        "message": "this is a trips page"
    }
@app.post("/login")
def login():
    return {
        "message": "this is a login page"
    }
@app.post("/register")
def register():
    return {
        "message": "this is a register page"
    }
@app.get("/weather")
def weather():
    return {
        "message": "this is a weather page"
    }
@app.get("/hotels")
def hotels():
    return {
        "message": "this is a hotels page"
    }
