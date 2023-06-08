import json
import random
import pytest

def get_questions(quantity: int):
	'''
	Returns randomly chosen questions from questions.json file in materials folder.

			Parameters:
					quantity (int): Number of questions chosen from database

			Returns:
					questions (list): List of questions for Voight-Kampff test
	'''
	with open('../../materials/questions.json') as f:
		questions = json.loads(f.read())
	return random.choices(questions, k=min(len(questions), quantity))

def write_questions(answers_info):
	'''
    Converts list of answers (with physical characteristics) to json and writes
	to an answers.json file in materials folder.

            Parameters:
                    answers_info (list): List of subjects' answers (with physical 
					characteristics)
    '''
	with open('../../materials/answers.json', 'w') as f:
		f.write(json.dumps(answers_info, indent=2))

def get_valid_int_answer(output_text: str, lower_boundary: int, higher_boundary: int) -> int:
	'''
	Expects correct integer input

			Parameters:
					output_text (str): Text which will be displayed before input
					lower_boundary (int): Minimal value of expected integer
					higher_boundary (int): Maximal value of expected integer

			Returns:
					answer (int): Valid integer
	'''
	while True:
		try:
			answer = int(input(output_text))
		except ValueError:
			print(f"Please enter a valid integer [{lower_boundary}...{higher_boundary}]")
			continue
		if answer >= lower_boundary and answer <= higher_boundary:
			return answer
		else:
			print(f'The integer must be in the range [{lower_boundary}...{higher_boundary}]')


def get_answer(question_info, answers_info):
	'''
	Gets subjects' answer to a question and physical characteristics from interviewer

			Parameters:
					question_info (dict): Current question information from database
					answers_info (list): List of subjects' answers (with physical 
					characteristics)
	'''
	print('Replicant answer =======>', question_info["answer"])
	answer = get_valid_int_answer("Enter subjects\' answer (0, 1, 2): ", 0, 2) == question_info["answer"]
	resp = get_valid_int_answer("Respiration (measured in BPM, normally around 12-16 breaths per minute): ", 12, 30)
	heart_rate = get_valid_int_answer("Heart rate (normally around 60 to 100 beats per minute): ", 60, 180)
	blush = get_valid_int_answer("Blushing level (categorical, 6 possible levels): ", 0, 6)
	dilation = get_valid_int_answer("Pupillary dilation (current pupil size, 2 to 8 mm): ", 2, 8)

	answers_info.append(dict(id=question_info["id"], answer=answer, resp=resp, heart_rate=heart_rate, blush=blush, dilation=dilation))
	print(answers_info)
	print('Answer has been recorded')

def quiz():
	'''
	Starts the quiz, prints questions and variants, gets answers and writes them
	'''
	answers_info = []
	num_of_questions = 3
	random_questions = get_questions(num_of_questions)
	for question in random_questions:
		print('\n', '='*120)
		print('Question: ', question["question"])
		for i, answer_variant in enumerate(question["variants"]):
			print(f'{i}. {answer_variant}')
		get_answer(question, answers_info)
	write_questions(answers_info)

def testing_answers():
	'''
	Starts tests, which will show weather subject considered replicant or human
	'''
	retcode = pytest.main(['test.py', '-s'])
	if retcode == pytest.ExitCode["OK"]:
		print('Subject considered as replicant')
	else:
		print('Subject considered as human')


if __name__ == '__main__':
	quiz()
	testing_answers()