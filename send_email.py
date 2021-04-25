import os
import time
import sys
import smtplib
import pytz
from datetime import datetime
from os import path
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.mime.base import MIMEBase 
from email import encoders

class Constants(object):
	def __init__(self):
		super(Constants, self).__init__()
		self._filename = []
		self._from_address = "youremail@gmail.com"
		self._email_subject = "Automated email with Python"
		self._email_body = "Hi, This is an automated mail. Please do ot reply."
		self._email_password = "yourpassword"
		self._to_address = ["youremail2@gmail.com","youremail3@gmail.com"]

	@property
	def repository(self):
		return self._repository

	@property
	def filename(self):
		return self._filename

	@property
	def directory(self):
		return self._directory

	@property
	def command(self):
		return self._command

	@property
	def to_address(self):
		return self._to_address

	@property
	def from_address(self):
		return self._from_address

	@property
	def email_body(self):
		return self._email_body

	@property
	def email_subject(self):
		return self._email_subject

	@property
	def email_password(self):
		return self._email_password

class Email(object):
	def __init__(self):
		super(Email, self).__init__()
		self._to_address = None
		
	@property
	def to_address(self):
		return self._to_address
	
	@to_address.setter
	def to_address(self,email):
		self._to_address = email

	def checkSize(self,r):
		size = 0
		try:
			for file in r:
				file = file
				size += os.stat(file).st_size
			print(size)
		except Exception as e:
			print(e)
			return False
		if size > 25000000:
			return False
		return True
		
	def sendemail(self,from_address,email_password,email_subject,email_body,attachment_filename):
		to_address = self._to_address	

		msg = MIMEMultipart()
		msg['From'] = from_address
		msg['To'] = ", ".join(to_address)
		msg['Subject'] = email_subject		

		msg.attach(MIMEText(email_body, 'html'))
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		s.login(from_address, email_password)
		text = msg.as_string()
		s.sendmail(from_address, to_address, text)
		s.quit()
		print("Email sent to "+str(to_address))

class Server(object):
	def __init__(self):
		super(Server, self).__init__()		
	
	def run(self,command):
		os.system(command)

class Project(object):
	def __init__(self):
		super(Project, self).__init__()
		self._server = Server()
		self._constants = Constants()
		self._email = Email()
		
	@property
	def server(self):
		return self._server
	
	@property
	def constants(self):
		return self._constants

	@property
	def email(self):
		return self._email

class Main(object):
	def __init__(self):
		super(Main, self).__init__()
		self._project = Project()

	def runServer(self):
		project = self._project
		try:
			print("Sending Email")
			project.email.to_address = project.constants.to_address
			e_from = project.constants.from_address
			e_pass = project.constants.email_password

			print("From: ",e_from,"\tTo: ",project.email.to_address,"\tPass: ",e_pass)

			UTC = pytz.utc
			IST = pytz.timezone('Asia/Kolkata')
			datetime_ist = datetime.now(IST)
			e_sub = project.constants.email_subject
			e_body = project.constants.email_body
			e_file = []
			time.sleep(5)
			project.email.sendemail(e_from,e_pass,e_sub,e_body,e_file)
			
		except Exception as e:
				print(e)

	def schedule(self,sch):
		project = self._project
		while True:
			try:
				now = datetime.now()
				if now.hour==int(sch.split(':')[0]) and now.minute==int(sch.split(':')[1]):
					time.sleep(3)
					self.runServer()
				time.sleep(30)
			except Exception as e:
				print(e)
				time.sleep(100)

if __name__ == '__main__':
	main = Main()
	main.schedule(sys.argv[1])
