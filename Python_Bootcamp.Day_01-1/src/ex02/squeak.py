def decorator(func):
    def print_squeak(*args, **kwargs):
        print("SQUEAK")
        return func(*args, **kwargs)
    return print_squeak


@decoratordef 
def add_ingot(purse: dict[str, int]) -> dict:
	new_dict: dict[str, int] = purse.copy()
	new_dict['gold_ingots'] = new_dict.get('gold_ingots', 0) + 1    
	return new_dict


@decoratordef 
def get_ingot(purse: dict[str, int]) -> dict:
	new_dict: dict[str, int] = purse.copy()
	new_dict['gold_ingots'] = new_dict.get('gold_ingots', 0) - 1    
	return new_dict


@decoratordef 
def empty(purse: dict[str, int]) -> dict:
	return {}