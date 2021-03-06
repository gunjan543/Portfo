from flask import Flask, render_template,request,redirect
import csv
app = Flask(__name__)
#print(app)
@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/<string:pagename>')
def works(pagename):
	return render_template(pagename)

def write_to_file(data):
	with open("database.txt",  mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["Message"]
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open("database.csv",newline='', mode='a') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["Message"]
		csv_writer = csv.writer(database2, delimiter =',', quotechar = '"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('/ThankYou.html')
		except:
			return "giberish"
		else:
			return 'Something went wrong, try again!'