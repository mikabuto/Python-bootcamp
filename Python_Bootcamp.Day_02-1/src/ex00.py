class Key:
	passphrase = "zax2rulez"

	def __gt__(self, other):
		return 9001 > other

	def __len__(self):
		return 1337  
  
	def __str__(self):
		return "GeneralTsoKeycard"    

	def __getitem__(self, key):
		return 3
	

def tests():
	key = Key()
	assert(len(key) == 1337)
	assert(key[404] == 3)
	assert(key > 9000)
	assert(key.passphrase == "zax2rulez")
	assert(str(key) == "GeneralTsoKeycard")
	print("SUCCESS")


tests()