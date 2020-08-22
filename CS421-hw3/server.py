from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)

db_name = 'grades.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
db = SQLAlchemy(app)

class Student(db.Model):
	studID = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	grade = db.Column(db.Integer)
	
	def __init__(self, name, grade):
		self.name = name
		self.grade = grade

db.create_all()

@app.route('/results', methods=['GET','POST'])
def results():
	if request.method == "POST":
		req = dict(request.form)
		res = Student.query.filter_by(studID=req["id"]).first()
		if res != None:
			res.name = req['name']
			res.grade = req['grade']
			db.session.commit()
	req=dict(request.args)
	if ('lowest' in req and req['lowest'] != "All"):
		students = Student.query.filter(Student.grade > 85).all()
	else:
		students = Student.query.all()
	return render_template('results.html', students = students)

@app.route('/', methods=['GET','POST'])
def homepage():
	if request.method == "POST":
		req = dict(request.form)
		if req['Student'] == "Add":
			stu = Student(req['name'], req['grade'])
			db.session.add(stu)
		elif req['Student'] == "Remove":
			res = Student.query.filter_by(studID=req["id"]).first()
			if res != None:
				db.session.delete(res)
		db.session.commit()
	return render_template('home.html', students = Student.query.all())
	
app.run()