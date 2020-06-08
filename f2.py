from flask import Flask
app = Flask(__name__)  # still relative to module

@app.route("/")
def hello():
    return "i m fine"

@app.route("/s")
def like():
    return "i like ice-cream"
app.run(debug=True)