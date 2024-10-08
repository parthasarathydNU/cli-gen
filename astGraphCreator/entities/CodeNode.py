class CodeNode:
    def __init__(self, node_type, name, location):
        self.type = node_type
        self.name = name
        self.location = location
        self.properties = {}
        self.relationships = []
        self.id = f"{self.type}_{self.name}_{self.location}"
