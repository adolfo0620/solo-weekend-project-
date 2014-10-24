
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
	return input("[1] Calculate a Car loan\n[2] Calculate a Mortgage\n[3] Update your profile\n[4] To Quite BudgetPAL\nEnter Your Answer: ")

def last_screen(user_name):
	print("Have a nice day %s" % user_name)