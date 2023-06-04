import wikipediaapi
import argparse
import json
import os
import sys
import logging

# function to check -d (depth) value
def check_value(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is an invalid positive int value")
    return ivalue

# parsing
parser = argparse.ArgumentParser()
parser.add_argument("-p", help="wiki article name", type=str, default='Feminism')
parser.add_argument("-d", help="parsing depth", type=check_value, default=3)
args = parser.parse_args()

g_start_article_name = args.p
g_depth = args.d

g_pages_dict = dict()
g_wiki = wikipediaapi.Wikipedia('en')

# _______________________________
# quiсk args parsing test:
# print('args: ', g_start_article_name, "and", g_depth)
# _______________________________   


# function to convert map to json and safe into wiki.json
def save_json(data: map):
	file_dir = os.path.dirname(__file__)
	file_name = os.path.join(file_dir, '../../misc/wiki.json')
	with open(file_name, 'w', encoding="utf8") as outfile:
		json.dump(data, outfile, indent=2)

# _______________________________
# array: list = ["hehe", 'haha', 'hoho', "sheeesh"]
# key: str = 'yes'
# data: map = {"a": [0,1,2], "b": 12, key: array}
# save_json(data)
# _______________________________



# Function for extracting all wiki links from this page 
# and writing results in g_pages_wiki

g_index = 0

def write_pages(wiki_page):
	if (wiki_page.exists()):
		global g_index
		logger.info(f"{g_index}\tvisiting page: {wiki_page.title}")
		g_index += 1
		# g_pages_dict[wiki_page] = list(wiki_page.links.values())[50:52]
		g_pages_dict[wiki_page] = list(wiki_page.links.values())

def dfs(start, visited=None, depth=g_depth):
	if visited is None:
		visited = set()
		visited.add(start.title)
		write_pages(start)
	if (depth == 0):
		return
	if (len(visited) > 1000):
		print('too many pages, try another article or another depth')
		return
	global g_pages_dict
	# print('\n=====================================\n',g_pages_dict[start], '\n!!!!!!!!!!!!!!!!!!!!\n')
	for inner_page in g_pages_dict.get(start, []):
		title = inner_page.title
		if title not in visited:
			visited.add(title)
			write_pages(inner_page)
			dfs(inner_page, visited, depth-1)


# g_pages_dict consists of WikipediaPage elements, this function converts
# them to titles (this data will be written in json file)

def prepareJSON(wiki_pages_dict) -> dict[str, list[str]]:
	return dict(map(lambda page: (page[0].title, list(map(lambda x: x.title, page[1]))), wiki_pages_dict.items()))

if __name__ == "__main__":

	logging.basicConfig(level=logging.INFO, stream=sys.stdout)
	logging.getLogger("wikipediaapi").setLevel(logging.WARNING)
	logger = logging.getLogger('wiki_parsing')

	dfs(g_wiki.page(g_start_article_name))
	save_json(prepareJSON(g_pages_dict))
