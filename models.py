import sqlite3
import datetime
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in("adolfo0620", "j57a6gvztr")

defaultdb = "budget.db" 

class User:
	def __init__(self):
		self.screen_name = ""
		self.first_name = ""
		self.last_name = ""
		self.credit_score = 0
		self.user_id = 0
		self.bank_name = ""
		#might delete these
		self.cash_in_hand = 0
		self.checking_account =""
		self.saving_account =""
		#might delete these
		self.credit_card_dues = 0
		self.car_loan_dues = 0
		self.mortgage_loan_dues = 0
		self.rent = 0
		self.student_loan = 0
		self.business_loan = 0

	def set_user_info(self,screen_name,first_name,last_name,credit_score):
		self.screen_name = screen_name
		self.first_name = first_name
		self.last_name = last_name
		self.credit_score = credit_score
		self.user_id = 0

	# connects to db and creates a income row for new user
	def create_incomes_for_new_user(self):
		conn = sqlite3.connect(defaultdb)
		c = conn.cursor()
		# insert wouldnt work beacuase rhis culom doesnt exits need to create a bank row  when user is created and instead of insert is to be update 
		statement = "INSERT INTO Incomes(cash_in_hand,checking_account,saving_account,user_id) VALUES(?,?,?,?);"
		c.execute(statement,(self.cash_in_hand,self.checking_account,self.saving_account,self.user_id,))
		conn.commit()
		c.close()

	def fetch_incomes_data(self):
		conn = sqlite3.connect(defaultdb)
		c =conn.cursor()
		statement = "SELECT * FROM Incomes  WHERE Incomes.user_id = (?)"
		c.execute(statement,(self.user_id,))
		income = c.fetchall()[0]
		self.cash_in_hand = income[1]
		self.checking_account = income[3]
		self.saving_account = income[4]
		self.bank_name = income[2]
		conn.commit()
		c.close()
		return(self.cash_in_hand,self.bank_name,self.checking_account,self.saving_account)

	#connects to db and creates a expense row for new new user
	def create_expenses_for_new_user(self):
		conn = sqlite3.connect(defaultdb)
		c = conn.cursor()
		statement = "INSERT INTO Expenses(credit_card_dues,car_loan_dues,mortgage_loan_dues,rent,student_loan,business_loan,user_id) VALUES(?,?,?,?,?,?,?);"
		c.execute(statement,(self.credit_card_dues,self.car_loan_dues,self.mortgage_loan_dues,self.rent,self.student_loan,self.business_loan,self.user_id))
		conn.commit()
		c.close()

	def fetch_expenses_data(self):
		conn = sqlite3.connect(defaultdb)
		c = conn.cursor()
		statement ="SELECT * FROM Expenses Where Expenses.user_id = (?)"
		c.execute(statement,(self.user_id,))
		expenses = c.fetchall()[0]
		credit_card_dues = expenses[1]
		car_loan_dues = expenses[2]
		mortgage_loan_dues = expenses[3]
		rent = expenses[4]
		student_loan = expenses[5]
		business_loan = expenses[6]
		conn.commit()
		c.close()
		return(credit_card_dues,car_loan_dues,mortgage_loan_dues,rent,student_loan,business_loan)

	#connects to db and updates user info
	def update_user(self):
		pass

 	# updates incomes
	def update_incomes(self,cash_in_hand,bank_name,checking_account,saving_account):
		conn = sqlite3.connect(defaultdb)
		c = conn.cursor()
		statement = "UPDATE Incomes SET cash_in_hand =(?),bank_name=(?),checking_account =(?),saving_account=(?) Where Incomes.user_id =(?)"
		c.execute(statement,(cash_in_hand,bank_name,checking_account,saving_account,self.user_id),)
		conn.commit()
		c.close()

	def update_expenses(self,credit_card_dues,car_loan_dues,mortgage_loan_dues,rent,student_loan,business_loan):
		conn = sqlite3.connect(defaultdb)
		c = conn.cursor()
		statement = "UPDATE Expenses Set credit_card_dues=(?),car_loan_dues=(?),mortgage_loan_dues=(?),rent=(?),student_loan=(?),business_loan=(?) WHERE Expenses.user_id=(?)"
		c.execute(statement,(credit_card_dues,car_loan_dues,mortgage_loan_dues,rent,student_loan,business_loan,self.user_id,))
		conn.commit()
		c.close()

	#create new user in db
	def create_user_in_db(self):
		conn = sqlite3.connect(defaultdb)
		c = conn.cursor()
		statement = "INSERT INTO Users(first_name,last_name,screen_name,credit_score) VALUES(?,?,?,?);"
		c.execute(statement,(self.first_name,self.last_name,self.screen_name,self.credit_score,))
		conn.commit()
		c.close()

	def fetch_user_info(self,screen_name):
		conn = sqlite3.connect(defaultdb)
		c = conn.cursor()
		statement = "SELECT first_name,last_name,credit_score FROM Users WHERE Users.screen_name=(?)"
		c.execute(statement,(screen_name,))
		self.screen_name = screen_name
		user_info = c.fetchall()[0]
		self.first_name = user_info[0]
		self.last_name = user_info[1]
		self.credit_score = user_info[2]
		conn.commit()
		c.close()

	def fetch_user_id(self):
		conn = sqlite3.connect(defaultdb)
		c = conn.cursor()
		statement = "SELECT id FROM Users Where Users.screen_name = (?)"
		c.execute(statement,(self.screen_name,))
		self.user_id = c.fetchone()[0]


	def get_balance(self):
		# return balance
		pass

class Budget:

	def __init__(self,credit_score):
		self.apr = 0.0
		self.two_year = 24
		self.three_year = 36
		self.five_year = 48

		if(eval(credit_score)>=740):
			self.apr = 0.04
		elif(eval(credit_score)>=700):
			self.apr = 0.07
		elif(eval(credit_score)>=660):
			self.apr = 0.1
		elif(eval(credit_score)>=580):
			self.apr = 0.15
		elif(eval(credit_score)<580):
			self.apr = 0.20
	
	def calculate_loan(self, loanAmount, interestRate, numberMonths):
		interestRate = interestRate/12
		round_bracket = pow((1+interestRate),numberMonths)
		first_bracket = interestRate * pow((1+interestRate),numberMonths)
		second_bracket = pow((1 + interestRate ),numberMonths) - 1
		answer = loanAmount * first_bracket / second_bracket
		return "{:.2f}".format(answer)

	#helper to get balance from bank accounts
	def get_balance_from_bank(self,bank_name,wire_num):
		bankdb = bank_name +".db"
		conn = sqlite3.connect(bankdb)
		c = conn.cursor()
		statement = "SELECT balance From accounts WHERE accounts.wire_num=(?)"
		c.execute(statement,(wire_num,))
		bal = c.fetchone()[0]
		return(bal)

	# to sum all expenses and income
	def sum_expenses(self,user_id):
		conn = sqlite3.connect(defaultdb)
		c = conn.cursor()
		statement ="SELECT * From Expenses WHERE Expenses.user_id=(?)"
		c.execute(statement,(user_id,))
		expense = c.fetchall()[0]
		total = 0
		for i in range(1,len(expense)-1):
			total += expense[i]
		conn.commit()
		c.close()
		return(total)

	def sum_income(self,cash_in_hand,bank_name,wire_numS,wire_numC):
		saving_bal = self.get_balance_from_bank(bank_name,wire_numS)
		checking_bal = self.get_balance_from_bank(bank_name,wire_numC)
		total = cash_in_hand+saving_bal+checking_bal
		return total

	def plot_diff(self,Month1,Month2, array_1 ,array_2):
		months = [Month1,Month2]
		trace1 = Bar(
			x=months,
			y=array_1,
			name='earn'
		)
		trace2 = Bar(
			x=months,
			y=array_2,
			name='lost'
		)
		data = Data([trace1, trace2])
		layout = Layout(
			barmode='group'
		)
		fig = Figure(data=data, layout=layout)
		plot_url = py.plot(fig, filename='grouped-bar')





