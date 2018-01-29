# start code here...
def ask_question():
	user_question=input("What is your question?")
	return user_question

def check_question(user_question):
	if user_question[-1]=="?":
		pass 
	else: 
		print("I'm sorry, I can only answer questions")

my_boolean=True

while my_boolean == True: 
	user_question=ask_question()
	if user_question == "quit":
		my_boolean = False 
	else:
		check_question(user_question)
