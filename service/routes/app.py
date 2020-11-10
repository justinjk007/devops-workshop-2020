from flask import Flask
from flask import jsonify
from service import routes

app= Flask(__name__)

@app.route("/")
def index():
    return("Hello from flask")

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
