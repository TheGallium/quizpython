import pick
import os

class ask():
	def question(question: str):
		user_responce = input(f'\n {question}\n\n > ')
		os.system('cls')
		os.system('clear')
		return user_responce

	def choice(question: str, options, default_choice: int = 1):
		selected_option, index = pick.pick(options, question, indicator = f'>', default_index = default_choice - 1)
		os.system('cls')
		os.system('clear')
		return selected_option
