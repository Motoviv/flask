#clrean blog
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from  datetime import datetime
import pymysql as cleanblog

app = Flask(__name__, template_folder='templete')  # still relative to module
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:@localhost/clean blog'
db = SQLAlchemy(app)

class Contact(db.Model):
    SNo = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    phone_num = db.Column(db.String(12),nullable=False)
    msg = db.Column(db.String(120),nullable=False)
    date = db.Column(db.String(12),nullable=True)
    email = db.Column(db.String(120),nullable=False )

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/contact",methods= ['GET','POST'])
def contact():
    if(request.method=='POST'):
        #add entry to the database
       name =request.form.get('name')
       email=request.form.get('email')
       phone =request.form.get('phone')
       message=request.form.get('message')

       entry=Contact(name=name,phone_num=phone,msg=message,date=datetime.now(),email=email)
       db.session.add(entry)
       db.session.commit()

    return render_template('contact.html')

app.run(debug=True)