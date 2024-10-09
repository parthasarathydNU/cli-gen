class CodeNode:
    def __init__(self, node_type, name, location, file_path):
        self.type = node_type
        self.name = name
        self.location = location
        self.file_path = file_path
        self.properties = {}
        self.relationships = []
        self.id = f"{self.type}_{self.name}_{self.location}"
