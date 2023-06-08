import json
import pytest

@pytest.fixture
def answers_fixture():
	with open('answers.json', 'r') as f:
		answers = json.loads(f.read())
	return answers

@pytest.fixture
def first_fixture(answers_fixture):
	if isinstance(answers_fixture, list):
		return answers_fixture[0]
	return None

@pytest.fixture
def second_fixture(answers_fixture):
	if isinstance(answers_fixture, list) and len(answers_fixture) > 1:
		return answers_fixture[1]
	return None

@pytest.fixture
def third_fixture(answers_fixture):
	if isinstance(answers_fixture, list) and len(answers_fixture) > 2:
		return answers_fixture[2]
	return None

@pytest.mark.parametrize("item", ["first_fixture", "second_fixture", "third_fixture"])
def test_awesome(item, request):
	answer = request.getfixturevalue(item)
	if (not answer):
		assert False
	print('-----', answer)
	if (answer.get("answer", False) == False):
		assert False
	if (answer.get("resp", 17) > 16 or answer.get("heart_rate", 101) > 100 
     	or answer.get("blush", 5) > 4 or answer.get("dilation", 6) > 5):
		print('Subject is lying')
		assert False
	assert True
