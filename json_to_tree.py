import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import json

file = open("data.json", "r")
data = json.load(file)
#data = {}

def add_nodes_with_properties(graph, data, parent_id=None, depth=0):
    """ Recursively adds nodes and edges to the graph, labeling each node with its key and properties """
    for key, value in data.items():
        node_id = f"{value['key']}_{depth}"
        # Node label includes the key and a summary of its properties
        node_label = f"{value['key']}\nChildren: {len(value['children'])}\nIsWord: {value.get('isWord', False)}"
        graph.add_node(node_id, label=node_label)

        if parent_id is not None:
            graph.add_edge(parent_id, node_id)
        if 'children' in value:
            add_nodes_with_properties(graph, value['children'], node_id, depth + 1)

# Creating a new directed graph for the representation with properties
G_with_props = nx.DiGraph()

# Adding a null root node with properties
root_id = "null_0"
G_with_props.add_node(root_id, label="null\nChildren: 1\nIsWord: False")

# Adding other nodes with properties
add_nodes_with_properties(G_with_props, data['children'], parent_id=root_id)

# Plotting the updated tree with properties
plt.figure(figsize=(12, 8))
pos = graphviz_layout(G_with_props, prog='dot')
nx.draw(G_with_props, pos, with_labels=True, labels=nx.get_node_attributes(G_with_props, 'label'), 
        arrows=False, node_size=3000, node_color="lightblue", font_size=10)
plt.title("Tree Diagram with Node Properties", size=15)
plt.show()
