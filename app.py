# here flask is module and Flask is class
from flask import Flask
from flask import render_template

# stsrting an application
app = Flask(__name__)

# route is a part of url after domain name
# e.x. https://flask.palletsprojects.com/en
# here /en is a route
@app.route("/")
def hello_world():
    return render_template("home.html")

if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)