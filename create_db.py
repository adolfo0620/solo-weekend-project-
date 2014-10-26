import sqlite3

defaultdb = "budget.db"

def create_users_table():
	conn = sqlite3.connect(defaultdb)
	c = conn.cursor()
	c.execute("DROP TABLE IF EXISTS 'Users';")
	c.execute(""" CREATE TABLE 'Users'(
		'id' INTEGER,
		'screen_name' VARCHAR,
		'first_name' VARCHAR,
		'last_name' VARCHAR
		'email' VARCHAR,
		'updated_at' Date,
		'credit_score' VARCHAR,
		UNIQUE(screen_name),
		PRIMARY KEY ('id'))""")
	conn.commit()
	c.close()

def create_incomes_table():
	conn = sqlite3.connect(defaultdb)
	c = conn.cursor()
	c.execute("DROP TABLE IF EXISTS 'Incomes';")
	# might have to change INTEGER
	c.execute(""" CREATE TABLE 'Incomes'(
		'id' INTEGER,
		'cash_in_hand' INTEGER,
		'bank_name' VARCHAR,
		'checking_account' VARCHAR,
		'saving_account' VARCHAR,
		'user_id' INTEGER,
		PRIMARY KEY ('id'),
		FOREIGN KEY (user_id) REFERENCES Users(id)
		)""")
	conn.commit()
	c.close()

def create_expenses_table():
	conn = sqlite3.connect(defaultdb)
	c = conn.cursor()
	c.execute("DROP TABLE IF EXISTS 'Expenses';")
	# might have to change this to floats
	c.execute(""" CREATE TABLE 'Expenses'(
		'id' INTEGER,
		'credit_card_dues' INTEGER,
		'car_loan_dues' INTEGER,
		'mortgage_loan_dues' INTEGER,
		'rent' INTEGER,
		'student_loan' INTEGER,
		'business_loan' INTEGER,
		'user_id' INTEGER,
		PRIMARY KEY ('id'),
		FOREIGN KEY (user_id) REFERENCES Users(id))""")
	conn.commit()
	c.close()
def create_log_table():
	conn = sqlite3.connect(defaultdb)
	c = conn.cursor()
	c.execute("DROP TABLE IF EXISTS 'Logs';")

#create the tables Users, Incomes, Expenses
create_users_table()
create_expenses_table()
create_incomes_table()


# Insert adolfo's user info
first_name = "adolfo"
last_name = "reyes"
screen_name = "adolfo0620"
credit_score = 780
conn = sqlite3.connect(defaultdb)
c = conn.cursor()
statement = "INSERT INTO Users(first_name,last_name,screen_name,credit_score) VALUES(?,?,?,?);"
c.execute(statement,(first_name,last_name,screen_name,credit_score,))
conn.commit()
c.close()


cash_in_hand = 50
checking_account = "5456"
saving_account = "6566"
user_id = 1
conn = sqlite3.connect(defaultdb)
c = conn.cursor()
statement = "INSERT INTO Incomes(cash_in_hand,checking_account,saving_account,user_id) VALUES(?,?,?,?);"
c.execute(statement,(cash_in_hand,checking_account,saving_account,user_id,))
conn.commit()
c.close()

credit_card_dues = 50
car_loan_dues = 1000
mortgage_loan_dues = 0
rent = 500
student_loan = 1000
business_loan = 0
conn = sqlite3.connect(defaultdb)
c = conn.cursor()
statement = "INSERT INTO Expenses(credit_card_dues,car_loan_dues,mortgage_loan_dues,rent,student_loan,business_loan,user_id) VALUES(?,?,?,?,?,?,?);"
c.execute(statement,(credit_card_dues,car_loan_dues,mortgage_loan_dues,rent,student_loan,business_loan,user_id))
conn.commit()
c.close()
