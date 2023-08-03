
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello This my first python github actions"


if __name__=="__main__":
    app.run()
