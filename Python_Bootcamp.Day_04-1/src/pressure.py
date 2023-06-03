import random
import time

def emit_gel(step):
	pressure = 50
	while True:
		current_step = random.randint(0, step)
		sign = yield pressure
		print(f'got sign: {sign}\tcurrent_step: {current_step}\n')
		pressure += sign * current_step

def valve(gen):
	sign = 1
	pressure = next(gen)
	while True:
		if pressure < 10 or pressure > 90:
			print(f'pressure={pressure}')
			print('\n!!!!!!!!!!!!!!!!!!!EMERGENCY BREAK!!!!!!!!!!!!!!!!!!!')
			gen.close()
			break
		if pressure < 20 or pressure > 80:
			print('\n======================Change sign=================')
			sign = -(sign)
		print(f'pressure: {pressure}\tsending sign={sign}....')
		pressure = gen.send(sign)
		time.sleep(2)

gen = emit_gel(50)
valve(gen)
