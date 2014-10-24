import sqlite3
import datetime

defaultdb = "budget.db" 

class User:
	def __init__(self):
		self.screen_name = ""
		self.first_name = ""
		self.last_name = ""
		self.credit_score = 0
		self.user_id = 0

	def set_user_info(self,screen_name,first_name,last_name,credit_score):
		self.screen_name = screen_name
		self.first_name = first_name
		self.last_name = last_name
		self.credit_score = credit_score
		self.user_id = 0

	# connects to db and updates income
	def update_incomes(self):
		pass

	#connects to db and updates expenses
	def update_expenses(self):
		pass

	#connects to db and updates user info
	def update_user(self):
		pass

	#create new user in db
	def create_user(self,first_name,last_name,screen_name,credit_score):
		conn = sqlite3.connect(defaultdb)
		c = conn.cursor()
		statement = "INSERT INTO Users(first_name,last_name,screen_name,credit_score) VALUES(?,?,?,?);"
		c.execute(statement,(first_name,last_name,screen_name,credit_score,))
		conn.commit()
		c.close()

	def fetch_user_info(self,screen_name):
		conn = sqlite3.connect(defaultdb)
		c = conn.cursor()
		statement = "SELECT first_name,last_name,credit_score FROM Users WHERE Users.screen_name=(?)"
		c.execute(statement,(screen_name,))
		user_info = c.fetchall()[0]
		self.first_name = user_info[0]
		self.last_name = user_info[1]
		self.credit_score = user_info[2]
		conn.commit()
		c.close()

	# gets score
	def get_score(self):
		pass

	def get_balance(self):
		# return balance
		pass
