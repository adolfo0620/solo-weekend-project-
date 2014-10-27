def clear_screen():
	from blessings import Terminal
	print (Terminal().clear)

def welcome_screen():
	print("Welcome to Your Budget Friend ")
	return raw_input("Are you a new user or a returning user\n[1] I am a returning user\n[2] I am a new user\nEnter 1 or 2:  ")

def error_screen():
	print("you have enter a wrong key")

def new_user_screen():
	clear_screen()
	first_name = raw_input("Please enter your first name:  ")
	last_name = raw_input("Please enter your last name:  ")
	screen_name = raw_input("Please enter a screen name:  ")
	credit_score = raw_input("Please enter your credit score:  ")
	return(first_name,last_name,screen_name,credit_score)

def returning_user_screen():
	return raw_input("Please enter your screen name: ")

def main_screen(user_name):
	print("------------------------------------------------")
	print("Welcome! %s" % user_name)
	return raw_input("[1] View current profile\n[2] Calculate a Loan\n[3] Update your profile\n[4] Plot difference\n[5] To Quite \nEnter Your Answer: ")

def last_screen(user_name):
	print("Have a nice day %s" % user_name)

def cal_loan():
	clear_screen()
	return raw_input("How much do you want?: ")

def display_loan(playment_per_month,num_months):
	print("For {0} Months you pay ${1} each month".format(num_months,playment_per_month))

def update_user_info_income():
	clear_screen()
	cash_in_hand = raw_input("How much money you have on you?: ")
	name_of_bank = raw_input("what is the name of your bank: ")
	checking_account = raw_input("What is the routing number to your checking account: ")
	saving_account = raw_input("What is the routing number to your saving account: ")
	return(cash_in_hand,name_of_bank,checking_account,saving_account)

def update_user_info_expense():
	clear_screen()
	print("This is the expenses portion")
	print("Please enter zero if the field does not apply to you")
	credit_card_dues = raw_input("how much is your monthly credit card payments: ")
	car_loan_dues = raw_input("how much is your monthly car loan payments: ")
	mortgage_loan_dues = raw_input("How much is your monthly mortgage payment: ")
	rent = raw_input("How much you pay for rent: ")
	student_loan = raw_input("how much is your student loan payments: ")
	business_loan = raw_input("how much is your business loan payments: ")
	return(credit_card_dues,car_loan_dues,mortgage_loan_dues,rent,student_loan,business_loan)

def display_current_income_info(cash_in_hand,bank_name,checking_account,saving_account):
	clear_screen()
	print("Current cash on hand: ${:.2f}".format(cash_in_hand))
	print("Current bank is:{}".format(bank_name))
	print("Checking routing number is set to: {}".format(checking_account))
	print("Saving routing number is set to: {}".format(saving_account))

def display_current_expense_info(credit_card_dues,car_loan_dues,mortgage_loan_dues,rent,student_loan,business_loan):
	print("Credit card monthly payments is set to: ${:.2f}".format(credit_card_dues))
	print("Car loan monthly payments is set to: ${:.2f}".format(car_loan_dues))
	print("Mortgage monthly payments is set to: ${:.2f}".format(mortgage_loan_dues))
	print("Rent is set to: ${:.2f}".format(rent))
	print("Student monthly payments is set to: ${:.2f}".format(student_loan))
	print("Business monthly payments is set to: ${:.2f}".format(business_loan))
