from datetime import datetime, timedelta
import pytz
class DateCalc:
	def __init__(self, formData):
		self.dt1 = formData.dt1.data
		self.dt2 = formData.dt2.data
		self.tz1 = formData.zone1.data
		self.tz2 = formData.zone2.data
		self.action = formData.action.data
		self.fmt = formData.fmt
		self.time1 = self.TZtoUTC(self.dt1, self.tz1)
		self.time2 = self.TZtoUTC(self.dt2, self.tz2)
		self.delta = self.GetDelta(self.time1, self.time2)

	def GetDelta(self, time1, time2):
		if time1 == time2:
			raise ValueError("Both dates are same. Nothing to do")
		return abs(time2 - time1)

	#Converts time in the specified timezone to UTC time
	def TZtoUTC(self, strLocTime, strTz):
		pytzone = pytz.timezone(strTz)
		locTime = datetime.strptime(strLocTime, self.fmt)
		return pytzone.localize(locTime).astimezone(pytz.utc)

	def GetWeekDays(self, time1, time2):
		#find starting and ending dates
		if time2 > time1:
			endDt = time2
			startDt = time1
		else:
			endDt = time1
			startDt = time2
		#set numWeekDays to 0
		numWeekDays = 0
		#check each day for a weekday till we reach end date
		while(startDt < endDt):
			if startDt.isoweekday() in [1,2,3,4,5]:
				numWeekDays += 1
			startDt = startDt + timedelta(1)
		#return numWeekDays
		return numWeekDays

	def Calc(self):
		if self.action == 'numTotDays':
			return self.delta.days
		elif self.action == 'numCompWeeks':
			return self.delta.days/7
		elif self.action == 'numWeekDays':
			return self.GetWeekDays(self.time1, self.time2)
		elif self.action == 's':
			return self.delta.total_seconds()
		elif self.action == 'm':
			return self.delta.total_seconds()/60.0
		elif self.action == 'h':
			return self.delta.total_seconds()/3600.0
		elif self.action == 'y':
			#secs in 1 year = secs in 1 hour * 24 hours * 365 days
			return self.delta.total_seconds()/(3600.0*24*365)
		return "Something bad has happened"
