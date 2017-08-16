from flask import Flask, flash, request, render_template
from wtforms import Form, StringField, DateTimeField, SelectField, SubmitField,validators, ValidationError
from os import urandom
from datetime import datetime
import pytz
from datecalc import DateCalc

app = Flask(__name__)
app.secret_key = urandom(24)
FMT="%Y-%m-%d %H:%M:%S"

def checkDate(form, field):
	#try to convert to datetime using FMT format
	try:
		datetime.strptime(field.data, FMT)
	except:
		raise ValidationError('Invalid Date or Date Format')

class DateForm(Form):
	actions = 	[	('numTotDays','Total Days'),
					('numCompWeeks','Complete Weeks'),
					('numWeekDays', 'Week Days'),
					('s','Seconds'), ('m','Minutes'),
					('h','Hours'), ('y','Years') ]
	dt1 = StringField('DateTime1',[checkDate])
	dt2 = StringField('DateTime2',[checkDate])
	zone1 = SelectField('Zone1')
	zone2 = SelectField('Zone2')
	action = SelectField('Find', choices=actions)
	submit = SubmitField('Calculate')
	fmt = FMT
	msg = ''

@app.route('/', methods=['POST', 'GET'])
def handle_dates():
	myform = DateForm(request.form)
	#collect all possible timezones
	zones = [('UTC','UTC')] + [(z,z) for z in pytz.common_timezones if not z=='UTC']
	#fill up zone1 and zone2 with our collected timezones
	myform.zone1.choices = myform.zone2.choices = zones
	if request.method=='GET':
		myform.dt1.data = datetime.strftime(datetime.now(), FMT)
		myform.dt2.data = datetime.strftime(datetime.now(), FMT)
	if request.method=='POST' and myform.validate():
		try:
			#DateCalc class does all date calculations
			dc = DateCalc(myform)
			myform.msg = dc.Calc()
		except ValueError as err:
			myform.msg = err
	return render_template('dates.html', form = myform)
	
app.run(debug=True)
