from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloIndex():
     return "Hello Cristi!"

app.run(host='0.0.0.0', port=5000)
