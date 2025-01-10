from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  print("This came from Python")
  return "Hello World!"

app.run()