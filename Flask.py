from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloIndex():
     return "Hello world2!"

app.run(host='0.0.0.0', port=5000)
