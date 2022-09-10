import random

user_name = input('What is your name?')
response_dict = {1:['a1','b1','c1'],
								 2:['a2','b2','c2'],
								 3:['a3','b3','c3'],
								 4:['hi']}

def bot_response():
	key = random.choice(list(response_dict.keys()))
	return random.choice(list(response_dict[key]))

while True:
	prompt = input(bot_response() + '\n')
	if prompt == 'exit':
		break