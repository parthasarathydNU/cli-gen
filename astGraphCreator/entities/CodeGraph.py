class CodeGraph:
    def __init__(self):
        self.nodes = {}  # Dictionary to store nodes by their IDs
        self.relationships = []  # List to store relationships

    def add_node(self, node):
        self.nodes[node.id] = node  # Store node by its ID

    def add_relationship(self, from_node_id, to_node_id, relationship_type):
        self.relationships.append((from_node_id, to_node_id, relationship_type))
