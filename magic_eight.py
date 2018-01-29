# start code here...

import random


def ask_question():
	user_question=input("What is your question?")
	return user_question

def add_questions():
	lst_of_responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good",
	"Very doubtful"]
	return random.choice(lst_of_responses)

def check_question(user_question):
	if user_question[-1]=="?":
		print(add_questions())
	else:
		print("I'm sorry, I can only answer questions")



my_boolean=True

while my_boolean == True:
	user_question=ask_question()
	if user_question == "quit":
		my_boolean = False
	else:
		check_question(user_question)
