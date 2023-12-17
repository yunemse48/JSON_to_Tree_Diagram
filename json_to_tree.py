import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import json

# Load data from JSON file
file = open("data.json", "r")
data = json.load(file)

def add_nodes_with_optional_properties(graph, data, parent_id=None, depth=0, show_properties=True):
    """ Recursively adds nodes and edges to the graph, with an option to include properties in labels """
    for key, value in data.items():
        node_id = f"{value['key']}_{depth}"

        if show_properties:
            # Node label includes the key and a summary of its properties
            node_label = f"{value['key']}\nChildren: {len(value['children'])}\nIsWord: {value.get('isWord', False)}"
        else:
            # Node label includes only the key
            node_label = f"{value['key']}"

        graph.add_node(node_id, label=node_label)

        if parent_id is not None:
            graph.add_edge(parent_id, node_id)
        if 'children' in value:
            add_nodes_with_optional_properties(graph, value['children'], node_id, depth + 1, show_properties)

# Option to show properties in the node labels
show_node_properties = True  # Set to False to hide properties

# Creating a new directed graph for the representation
G_with_props = nx.DiGraph()

# Adding a null root node with optional properties
root_id = "null_0"
root_label = "null\nChildren: 1\nIsWord: False" if show_node_properties else "null"
G_with_props.add_node(root_id, label=root_label)

# Adding other nodes with optional properties
add_nodes_with_optional_properties(G_with_props, data['children'], parent_id=root_id, show_properties=show_node_properties)

# Plotting the tree with optional properties
plt.figure(figsize=(12, 8))
pos = graphviz_layout(G_with_props, prog='dot')
nx.draw(G_with_props, pos, with_labels=True, labels=nx.get_node_attributes(G_with_props, 'label'), 
        arrows=False, node_size=3000, node_color="lightblue", font_size=10)
plt.title("Tree Diagram with Node Properties" if show_node_properties else "Tree Diagram", size=15)
plt.show()
