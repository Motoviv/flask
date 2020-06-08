from flask import Flask, render_template
app = Flask(__name__, template_folder='templete')  # still relative to module

@app.route("/")
def hello():
    return render_template('index1.html')

@app.route("/p")
def srija():
    name='Srija sinha' #vaiable
    return render_template('about1.html',name1=name)

@app.route("/n")
def b():
      return render_template('bootstrap.html')

app.run(debug=True)