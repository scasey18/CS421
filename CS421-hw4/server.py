from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)

db_name = 'records.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
db = SQLAlchemy(app)

class Record(db.Model):
	rID = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	email = db.Column(db.Text)
	phonenum = db.Column(db.Integer)
	address = db.Column(db.Text)
	
	def __init__(self, name, email, phonenum, address):
		self.name = name
		self.email = email
		self.phonenum = phonenum
		self.address = address

db.create_all()

@app.route('/results', methods=['GET','POST'])
def results():
	if request.method == "POST":
		req = dict(request.form)
		res = Record.query.filter_by(rID=req["id"]).first()
		if res != None:
			res.name = req['name']
			res.email = req['email']
			res.phonenum = req["phonenum"]
			res.address = req["address"]
			db.session.commit()
	return render_template('results.html', Records = Record.query.all())

@app.route('/', methods=['GET','POST'])
def homepage():
	if request.method == "POST":
		req = dict(request.form)
		if req['Record'] == "Add":
			stu = Record(req['name'], req['email'], req["phonenum"],req["address"])
			db.session.add(stu)
		elif req['Record'] == "Remove":
			res = Record.query.filter_by(rID=req["id"]).first()
			if res != None:
				db.session.delete(res)
		db.session.commit()
	return render_template('home.html')
	
app.run()