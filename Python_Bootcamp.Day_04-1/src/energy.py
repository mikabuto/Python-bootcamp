import itertools

def is_string(x):
	return type(x) == str

def fix_wiring(cables, sockets, plugs):
	for plug, socket, cable in itertools.zip_longest(filter(is_string, plugs), filter(is_string, sockets), filter(is_string, cables)):
		if (cable is None or socket is None):
			break
		elif (plug is None):
			yield f"weld {cable} to {socket} without plug"
		else:
			yield f"plug {cable} into {socket} using {plug}"
	

# plugs = ['plug1', 'plug2', 'plug3', 'plug4', 'plug5']
# sockets = ['socket1', 'socket2', 'socket3', 'socket4']
# cables = ['cable1', 'cable2', 'cable3', 'cable4']

plugs = ['plugZ', None, 'plugY', 'plugX']
sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
cables = ['cable2', 'cable1', False]

for c in fix_wiring(cables, sockets, plugs):
	print(c)