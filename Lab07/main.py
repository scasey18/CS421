from flask import Flask, render_template, request, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
Migrate(app,db)

class User(db.Model):
	__tablename__ = "users"
	
	id = db.Column(db.Integer, primary_key=True)
	firstN = db.Column(db.Text)
	lastN = db.Column(db.Text)
	email = db.Column(db.Text)
	password = db.Column(db.Text)
	
	def __init__(self, fName, lName, email, pwd):
		self.firstN = fName
		self.lastN = lName
		self.email = email
		self.password = pwd

db.create_all()

#Migrated and slightly changed from Lab06
def checkPassword(pwd):
	hasupper, haslower, endsNumber, length = False, False, False, False
	if len(pwd) >= 8:
		length = True
	for i in pwd:
		if i.isupper():
			hasupper = True
		elif i.islower():
			haslower = True
		if (hasupper == True and haslower == True):
			break
	if len(pwd) >= 1 and pwd[-1].isdigit():
		endsNumber = True
	if (hasupper == True and haslower == True and endsNumber == True and length == True):
		return True
	return False

@app.route('/signup', methods=['GET','POST'])
def signup():
	if request.method=="POST":
		req = dict(request.form)
		if (req['pwd'] == req['confirmPwd'] and checkPassword(req['pwd']) == True):
			new_user = User(req['fName'], req['lName'], req['email'], req['pwd'])
			db.session.add(new_user)
			db.session.commit()
			return redirect(url_for('thankyou'))
	return render_template('signup.html')
	
@app.route('/login', methods=['GET','POST'])
def login():
	if request.method=="POST":
		req = dict(request.form)
		acct = User.query.filter(User.email == req['email']).first()
		if acct.password == req['pwd']:
			return redirect(url_for('secret'))
	return render_template('login.html')

@app.route('/secretpage')
def secret():
	return render_template('secretPage.html')

@app.route('/thankyou')
def thankyou():
	return render_template('thankyou.html')

if __name__ == "__main__":
	app.run()