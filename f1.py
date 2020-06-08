from flask import Flask, render_template
app = Flask(__name__, template_folder='templete')  # still relative to module

@app.route("/")
def hello():
    return render_template('index1.html')

@app.route("/srija")
def srija():
    return render_template('about1.html')
app.run(debug=True)