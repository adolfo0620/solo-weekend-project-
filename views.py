
def welcome_screen():
	print("Welcome to You'r BudgetPAl ")
	return input("Are you a new user or a returning user\n[1] I am a returning user\n[2] I am a new user")

def error_screen():
	print("you have enter a wrong key")

def new_user_screen():
	first_name = input("Please enter your first name: ")
	last_name = input("Please enter your last name: ")
	screen_name = input("Please enter a screen name: ")
	credit_score = input("Please enter your credit score ")
	return(first_name,last_name,screen_name,credit_score)
