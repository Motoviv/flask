from flask import Flask, render_template
app = Flask(__name__, template_folder='templete')  # still relative to module

@app.route("/")
def hello():
    return render_template('index1.html')

@app.route("/p")
def c():
    name='Srija sinha' #vaiable
    return render_template('about1.html',name1=name)
app.run(debug=True)