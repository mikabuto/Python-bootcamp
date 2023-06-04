import json
import os
import networkx as nx
import matplotlib.pyplot as plt

file_dir = os.path.dirname(__file__)

# Defining a Class
class GraphVisualization:

	def __init__(self):
		
		# visual is a list which stores all
		# the set of edges that constitutes a
		# graph
		self.visual = []
		
	# addEdge function inputs the vertices of an
	# edge and appends it to the visual list
	def addEdge(self, a, b):
		temp = [a, b]
		self.visual.append(temp)
		
	# In visualize function G is an object of
	# class Graph given by networkx G.add_edges_from(visual)
	# creates a graph with a given list
	# nx.draw_networkx(G) - plots the graph
	# plt.show() - displays the graph
	def visualize(self):
		G = nx.Graph()
		G.add_edges_from(self.visual)
		nx.draw_networkx(G, font_size=8)
		file_name = os.path.join(file_dir, '../../misc/images/graph.png')
		# plt.figure(figsize=(5,4))
		plt.savefig(file_name, dpi=300, bbox_inches='tight')

# Driver code

file_name = os.path.join(file_dir, '../../misc/wiki.json')
with open(file_name) as f:
	json_file = f.read()
	data = json.loads(json_file)

G = GraphVisualization()

for parent in data:
	for child in data[parent]:
		G.addEdge(parent, child)

G.visualize()