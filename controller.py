import views
import models

current_user = models.User()
answer = views.welcome_screen()
if (eval(answer) == 1):
	print("answer was 1")
elif(eval(answer)==2):
	(first_name,last_name,screen_name,credit_score)=views.new_user_screen()
	current_user.set_user_info(first_name,last_name,screen_name,credit_score)
else:
	views.error_screen()