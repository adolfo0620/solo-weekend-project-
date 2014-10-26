import views
import models

current_user = models.User()
answer = views.welcome_screen()
if (eval(answer) == 1):
	screen_name = views.returning_user_screen()
	current_user.fetch_user_info(screen_name)
elif(eval(answer)==2):
	(first_name,last_name,screen_name,credit_score)=views.new_user_screen()
	current_user.set_user_info(screen_name,first_name,last_name,credit_score)
else:
	views.error_screen()

budget = models.Budget(current_user.credit_score)

in_use = True
while in_use == True:
	reply = views.main_screen(current_user.first_name)
	if(eval(reply)==1):
		print("enter 1")
	elif(eval(reply)==2):
		loan_amount = views.cal_loan()
		y2 = budget.calculate_loan(int(loan_amount),budget.apr,budget.two_year)
		y3 = budget.calculate_loan(int(loan_amount),budget.apr,budget.three_year)
		y5 = budget.calculate_loan(int(loan_amount),budget.apr,budget.five_year)
		views.display_loan(y2,budget.two_year)
		views.display_loan(y3,budget.three_year)
		views.display_loan(y5,budget.five_year)
	elif(eval(reply)==3):
		print("entered 3")
	elif(eval(reply)==4):
		in_use = False
views.last_screen(current_user.first_name)