from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/results', methods=['GET','POST'])
def results():
	if (request.method == 'POST'):
		hasupper, haslower, endsNumber, length = False, False, False, False
		uname = request.form.get('uname')
		pwd = request.form.get('pwd')
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
			return render_template('report.html', success = "Your Password passed the 4 requirements")
		reasons = ["Oh No! Looks like you had issues with your password!", "Here are the requirements you failed:"]
		if (hasupper == False):
			reasons.append("You did not use an uppercase letter")
		if (haslower == False):
			reasons.append("You did not use a lowercase letter")
		if (endsNumber == False):
			reasons.append("You did not end your password with a number")
		if length == False:
			reasons.append("Your password was not at least 8 characters long")
		return render_template('report.html', failed = reasons)
	return render_template('report.html')
	

@app.route('/')
def home():
	return render_template('index.html')
	
app.run()