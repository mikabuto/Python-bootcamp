import sys

limit = 0
if (len(sys.argv) > 1 and sys.argv[1].isnumeric()):
  limit = int(sys.argv[1])

lines = []
curr_line_number = 0

while True:
	try:
		user_input = input()
		curr_line_number += 1

		if (len(user_input) == 32 and user_input.startswith('00000') and user_input[5] != '0'):
			lines.append(user_input)
		if user_input == '' or curr_line_number == limit:
			break
	except (EOFError):
		break

print('\n'.join(lines))