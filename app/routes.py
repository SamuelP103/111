from flask import Flask 

app = Flask(__name__)

@app.get("/")
def index():
    me = {
        "first_name":"Billy",
        "last_name":"Bob",
        "hobbies":"fishing",
        "online": True,
    }
    return me