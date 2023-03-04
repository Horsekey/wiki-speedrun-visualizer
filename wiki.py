# libraries
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.pyplot import text, figure
import sys

"""
USAGE:

python3 wiki.py '<PASTED "Share Path">'

-h [display usage]

"""
# get all arguments
games = sys.argv[1:]

# Initialize empty list for multiple lists
lists = []

# Iterate through arguments, delimit items by comma and create list, add the created list to initial list
for arg in games:
    my_list = arg.split(",")
    print(my_list)
    lists.append(my_list)

# Print different games created
for i, lst in enumerate(lists):
    print(f"List {i+1}: {lst}")


node_list = {}

def create_graph(lists):
    node_list = {'from':[], 'to':[]}
    for list in lists:
        for index, elem in enumerate(list):
            if (index+1 < len(list) and index - 1 >= 0):
                prev_el = str(list[index-1])
                curr_el = str(elem)
                # next_el = str(list[index+1])
                node_list['from'].append(prev_el)
                node_list['to'].append(curr_el)
            
            elif index == len(list)-1:
                node_list['from'].append(str(list[index-1]))
                node_list['to'].append(elem)

    return node_list

# Iterate through the static list, figure out the previous current and next element, and append them to the respective keys
# UPDATE TO LOOP THROUGH 'lists' variable also may need to change how 'all_df' is created since we would have multiple starting and ending points

"""
for index, elem in enumerate(game1):
    if (index+1 < len(game1) and index - 1 >= 0):
        prev_el = str(game1[index-1])
        curr_el = str(elem)
        next_el = str(game1[index+1])
        all_df['from'].append(curr_el)
        all_df['to'].append(next_el)
"""

# This could probably use a different graph creation since we aren't using a pandas dataframe (which we might consider)

G=nx.from_pandas_edgelist(create_graph(lists), 'from', 'to')

print(G)

# this sucks remove it and make colors based on d.values() which are the nodes
'''
colors = []
for index, node in enumerate(G):
    # if the item is first in the chain
    if not index:
        colors.append("firebrick")
    # if the item is last in the chain
    elif index == len(games[game]) - 2:
        colors.append("")
    else:
        colors.append("tab:red")
'''

# Define the size of the matplotlib figure
figure(figsize=(250,250), dpi=10)

# define all connections in a dictionary
d = dict(G.degree)

# where the nodes will be placed on the matplotlib graph
pos = nx.spring_layout(G)

# Different way to draw the network
# nx.draw(G, with_labels=True, node_color=colors, pos=nx.fruchterman_reingold_layout(G))

# Draws the graph
nx.draw(G, pos=pos,node_color=[value for value in d.values()], with_labels=False, node_size=[len(key)*5000 for key in d], node_shape='o', font_color='white', cmap=plt.cm.Reds)

# Changes text size of all nodes
for node, (x, y) in pos.items():
    text(x, y, node, fontsize=50, ha='center', va='center', color='grey')

# Show the graph
plt.show()