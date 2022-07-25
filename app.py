from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import app_config

config_name = "development"

app = Flask(__name__, instance_relative_config=True )
app.config.from_object(app_config[config_name])

db = SQLAlchemy(app)

@app.route('/')
def loginpage():
    return render_template("auth/login.html")

@app.route('/login', methods=['POST'])
def login():
    user = request.form['user']
    return render_template('home/homepage.html', title="Welcome " + user , user=user)

@app.route('/homepage')
def homepage():
    user = "Sachin"
    return render_template('home/homepage.html', title="Dashboard" , user=user)

 
if __name__ == '__main__':
    app.run(debug=True)