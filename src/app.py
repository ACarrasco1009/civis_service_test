from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello!"

@app.route("/test")
def test():
    return "Test!"

if __name__ == '__main__':
    app.run(port=5000)
