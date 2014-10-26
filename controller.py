import views
import models

current_user = models.User()
answer = views.welcome_screen()
# returning user
if (eval(answer) == 1):
	screen_name = views.returning_user_screen()
	current_user.fetch_user_info(screen_name)
# creating new user 
elif(eval(answer)==2):
	(first_name,last_name,screen_name,credit_score)=views.new_user_screen()
	current_user.set_user_info(screen_name,first_name,last_name,credit_score)
	current_user.create_user_in_db()
else:
	views.error_screen()

current_user.fetch_user_id()
if(eval(answer)==2):
	current_user.create_incomes_for_new_user()
	current_user.create_expenses_for_new_user()
budget = models.Budget(current_user.credit_score)

in_use = True
while in_use == True:
	reply = views.main_screen(current_user.first_name)
	if(eval(reply)==1):
		(cash_in_hand,bank_name,checking_account,saving_account)=current_user.fetch_incomes_data()
		views.display_current_income_info(cash_in_hand,bank_name,checking_account,saving_account)
		(credit_card_dues,car_loan_dues,mortgage_loan_dues,rent,student_loan,business_loan)=current_user.fetch_expenses_data()
		views.display_current_expense_info(credit_card_dues,car_loan_dues,mortgage_loan_dues,rent,student_loan,business_loan)

	elif(eval(reply)==2):
		loan_amount = views.cal_loan()
		y2 = budget.calculate_loan(int(loan_amount),budget.apr,budget.two_year)
		y3 = budget.calculate_loan(int(loan_amount),budget.apr,budget.three_year)
		y5 = budget.calculate_loan(int(loan_amount),budget.apr,budget.five_year)
		views.display_loan(y2,budget.two_year)
		views.display_loan(y3,budget.three_year)
		views.display_loan(y5,budget.five_year)
	elif(eval(reply)==3):
		(cash_in_hand,bank_name,checking_account,saving_account)=views.update_user_info_income()
		current_user.update_incomes(cash_in_hand,bank_name,checking_account,saving_account)
		(credit_card_dues,car_loan_dues,mortgage_loan_dues,rent,student_loan,business_loan)=views.update_user_info_expense()
		current_user.update_expenses(credit_card_dues,car_loan_dues,mortgage_loan_dues,rent,student_loan,business_loan)
	elif(eval(reply)==4):
		in_use = False
views.last_screen(current_user.first_name)