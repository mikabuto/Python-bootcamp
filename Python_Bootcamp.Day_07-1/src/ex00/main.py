import json
import random
import pytest

answers_info = []

def get_questions(quantity):
	with open('questions.json') as f:
		questions = json.loads(f.read())
	return random.choices(questions, k=quantity)

def write_questions():
	with open('answers.json', 'w') as f:
		f.write(json.dumps(answers_info, indent=2))

def get_valid_int_answer(output_text: str, lower_boundary: int, higher_boundary: int) -> int:
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


def get_answer(question_info):
	print('=======>', question_info["answer"])
	answer = get_valid_int_answer("Enter subjects\' answer (0, 1, 2): ", 0, 2) == question_info["answer"]
	resp = get_valid_int_answer("Respiration (measured in BPM, normally around 12-16 breaths per minute): ", 12, 30)
	heart_rate = get_valid_int_answer("Heart rate (normally around 60 to 100 beats per minute): ", 60, 180)
	blush = get_valid_int_answer("Blushing level (categorical, 6 possible levels): ", 0, 6)
	dilation = get_valid_int_answer("Pupillary dilation (current pupil size, 2 to 8 mm): ", 2, 8)

	answers_info.append(dict(id=question_info["id"], answer=answer, resp=resp, heart_rate=heart_rate, blush=blush, dilation=dilation))
	print(answers_info)
	print('Answer has been recorded')

if __name__ == '__main__':
	num_of_questions = 3
	random_questions = get_questions(num_of_questions)
	for question in random_questions:
		print('\n', '='*120)
		print('Question: ', question["question"])
		for i, answer_variant in enumerate(question["variants"]):
			print(f'{i}. {answer_variant}')
		get_answer(question)
		write_questions()
	retcode = pytest.main(['test.py', '-s'])
	if retcode == pytest.ExitCode["OK"]:
		print('Subject considered as replicant')
	else:
		print('Subject considered as human')