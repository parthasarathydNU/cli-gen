import networkx as nx
from pyvis.network import Network

def visualize_graph_3d(code_graph):
    G = nx.DiGraph()
    
    # Add nodes
    for node_id, node in code_graph.nodes.items():
        G.add_node(node_id, label=node.name, type=node.type, location=node.location, file_path=node.file_path)
    
    # Add edges
    for from_node, to_node, rel_type in code_graph.relationships:
        G.add_edge(from_node, to_node, relationship=rel_type)
    
    # Create a Pyvis network
    net = Network(notebook=False)
    
    # Add nodes and edges to the Pyvis network
    for node in G.nodes(data=True):
        net.add_node(node[0], label=node[1]['label'], title=f"Type: {node[1]['type']}\nFile Path: {node[1]['file_path']}\nLocation: {node[1]['location']}", group=node[1]['file_path'])
        
    for edge in G.edges(data=True):
        net.add_edge(edge[0], edge[1], title=edge[2]['relationship'])
    
    # Enable physics to allow nodes to be dragged around
    net.show_buttons(filter_=['physics'])
    
    # Generate and show the network
    net.show("code_graph.html")
