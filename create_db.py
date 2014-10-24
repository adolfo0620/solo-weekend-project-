import sqlite3

defautdb = "budget.db"

def create_users_table():
	conn = sqlite3.connect(defautdb)
	c = conn.cursor()
	c.execute("DROP TABLE IF EXISTS 'Users';")
	c.execute(""" CREATE TABLE 'Users'(
		'id' INTEGER,
		'user_name' VARCHAR,
		'email' VARCHAR,
		'updated_at' Date,
		'wire_number' VARCHAR,
		'credit_score' VARCHAR,
		PRIMARY KEY ('id'))""")
	conn.commit()
	c.close()

def create_incomes_table():
	conn = sqlite3.connect(defautdb)
	c = conn.cursor()
	c.execute("DROP TABLE IF EXISTS 'Incomes';")
	# might have to change INTEGER
	c.execute(""" CREATE TABLE 'Incomes'(
		'id' INTEGER,
		'cash_in_hand' INTEGER,
		'checking_account' VARCHAR,
		'saving_account' VARCHAR,
		'monthy_earning' Real,
		'user_id' INTEGER,
		PRIMARY KEY ('id'),
		FOREIGN KEY (user_id) REFERENCES Users(id)
		)""")
	conn.commit()
	c.close()

def create_expenses_table():
	conn = sqlite3.connect(defautdb)
	c = conn.cursor()
	c.execute("DROP TABLE IF EXISTS 'Expenses';")
	# might have to change this to floats
	c.execute(""" CREATE TABLE 'Expenses'(
		'id' INTEGER,
		'credit_card_dues' INTEGER,
		'car_loan_dues' INTEGER,
		'mortage_loan_dues' INTEGER,
		'rent' INTEGER,
		'student_loan' INTEGER,
		'business_loan' INTEGER,
		'taxes' INTEGER,
		'user_id' INTEGER,
		PRIMARY KEY ('id'),
		FOREIGN KEY (user_id) REFERENCES Users(id))""")
	conn.commit()
	c.close()

#create the tables Users, Incomes, Expenses
create_users_table()
create_expenses_table()
create_incomes_table()
