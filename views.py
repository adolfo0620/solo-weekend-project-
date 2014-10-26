
def welcome_screen():
	print("Welcome to You'r BudgetPAL ")
	return input("Are you a new user or a returning user\n[1] I am a returning user\n[2] I am a new user\nEnter 1 or 2:  ")

def error_screen():
	print("you have enter a wrong key")

def new_user_screen():
	first_name = input("Please enter your first name:  ")
	last_name = input("Please enter your last name:  ")
	screen_name = input("Please enter a screen name:  ")
	credit_score = input("Please enter your credit score:  ")
	return(first_name,last_name,screen_name,credit_score)

def returning_user_screen():
	return input("Please enter your screen name: ")

def main_screen(user_name):
	print("Welcome back! %s" % user_name)
	return input("[1] Calculate a Car loan\n[2] Calculate a Loan\n[3] Update your profile\n[4] To Quite BudgetPAL\nEnter Your Answer: ")

def last_screen(user_name):
	print("Have a nice day %s" % user_name)

def cal_loan():
	return input("How much do you want?: ")

def display_loan(playment_per_month,num_months):
	print("For {0} Months you pay ${1} each month".format(num_months,playment_per_month))

def update_user_info_income():
	cash_in_hand = input("How much money you have on you?: ")
	checking_account = input("What is the rounting number to your checking account: ")
	saving_account = input("What is the rounting number to your saving account: ")

