gold_ingots = "gold_ingots"

def add_ingot(purse: dict[str, int]) -> dict[str, int]:
    new_purse = purse.copy()
    new_purse[gold_ingots] = new_purse.get(gold_ingots, 0) + 1
    return new_purse

def get_ingot(purse: dict[str, int]) -> dict[str, int]:
	new_purse = purse.copy()
	current_ingots = new_purse.get(gold_ingots, 0)
	if current_ingots:
		new_purse[gold_ingots] = current_ingots - 1
	return new_purse

def empty(purse: dict[str, int]):
	return {}
	

purse: dict[str, int] = {gold_ingots: 3}

print('==================================\n initial purse: \n', purse)
print('\nadd_ingot(get_ingot(add_ingot(empty(purse)))): \n', add_ingot(get_ingot(add_ingot(empty(purse)))))
print('\ninitial purse: \n', purse)

purse[gold_ingots] = 1
print('\n==================================\n initial purse: \n', purse)
print('\nget_ingot(get_ingot(get_ingot(purse))): \n', get_ingot(get_ingot(get_ingot(purse))))
print('\ninitial purse: \n', purse)

purse[gold_ingots] = 1
print('\n==================================\n initial purse: \n', purse)
print('\nget_ingot(add_ingot(get_ingot(get_ingot(purse)))): \n', get_ingot(add_ingot(get_ingot(get_ingot(purse)))))
print('\ninitial purse: \n', purse)
