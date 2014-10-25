import views
import models

current_user = models.User()
answer = views.welcome_screen()
if (eval(answer) == 1):
	screen_name = views.returning_user_screen()
	current_user.fetch_user_info(screen_name)
elif(eval(answer)==2):
	(first_name,last_name,screen_name,credit_score)=views.new_user_screen()
	current_user.set_user_info(first_name,last_name,screen_name,credit_score)
else:
	views.error_screen()
in_use = True
while in_use == True:
	reply = views.main_screen(current_user.first_name)
	if(eval(reply)==1):
		print("enter 1")
	elif(eval(reply)==2):
		print("entered 2")
	elif(eval(reply)==3):
		print("entered 3")
	elif(eval(reply)==4):
		in_use = False
views.last_screen(current_user.first_name)