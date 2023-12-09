# Importing the necessary libraries to execute the "Random Walk Method"
import networkx as nx
import random
import matplotlib.pyplot as plt
import operator
from tabulate import tabulate

#select random graph using gnp_random_graph() function of networkx
Graph = nx.gnp_random_graph(10, 0.5, directed=True)
plt.figure(figsize=(5,5)) # create the figure first
nx.draw(Graph, with_labels=True, node_color='green') #draw the network graph

nx.write_gexf(Graph, "random_graph.gexf") #save the graph in .gexf format

# random_node is the start node selected randomly
all_nodes = list(Graph.nodes())
random_node = random.choice(all_nodes)
dict_counter = {} #initialise the value for all nodes as 0
for i in range(Graph.number_of_nodes()):
    dict_counter[i] = 0
# increment by traversing through all neighbors nodes
dict_counter[random_node] = dict_counter[random_node]+1

#Traversing through the neighbors of start node
for i in range(1000):
    list_for_nodes = list(Graph.neighbors(random_node))
    if len(list_for_nodes)==0:# if random_node having no outgoing edges
        random_node = random.choice(all_nodes)
        dict_counter[random_node] = dict_counter[random_node]+1
        
    else:
        random_node = random.choice(list_for_nodes) #choose a node randomly from neighbors
        dict_counter[random_node] = dict_counter[random_node]+1
        
# using pagerank() method to provide ranks for the nodes        
rank_node = nx.pagerank(Graph)

#sorting the values of rank and random walk of respective nodes
sorted_rank = sorted(rank_node.items(), key=operator.itemgetter(1))
sorted_random_walk = sorted(dict_counter.items(), key=operator.itemgetter(1))

#displaying the results in tabular form
print("Graph:")
print(tabulate(list(Graph.degree()), headers=["Node", "Degree"], tablefmt="fancy_grid"))

print("Sorted Random Walk:")
print(tabulate(sorted_random_walk, headers=["Node", "Random Walk"], tablefmt="fancy_grid"))

print("Sorted Rank:")
print(tabulate(sorted_rank, headers=["Node", "Rank"], tablefmt="fancy_grid"))

plt.show() #to show the graph by plotting it
