limit = 3

lines = []
curr_line_number = 0

def print_error():
	print('Error')
	exit()

while True:
	try:
		user_input = input()
		curr_line_number += 1

		if curr_line_number > limit or len(user_input) != 5:
			print_error()
		lines.append(user_input)
	except (EOFError):
		break

answer = False
if len(lines) != 3:
	print_error()

if lines[0][0] == lines[0][4] == '*' and '*' not in lines[0][1:4]:
	if lines[1][0:2] == lines[1][3:5] == '**' and lines[1][2] != '*':
		if lines[2][0] == lines[2][2] == lines[2][4] == '*' and lines[2][1] != '*' and lines[2][3] != '*':
			answer = True

print(answer)