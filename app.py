# here flask is module and Flask is class
from flask import Flask

# stsrting an application
app = Flask(__name__)

# route is a part of url after domain name
# e.x. https://flask.palletsprojects.com/en
# here /en is a route
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)