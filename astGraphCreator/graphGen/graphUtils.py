from entities.CodeGraph import CodeGraph
from astParser.astParser import parse_ast

def generateGraph(ast_dict):
    
    code_graph = CodeGraph()

    for file_path, ast_json in ast_dict.items():
        graph = parse_ast(ast_json, file_path)
        code_graph.nodes.update(graph.nodes)
        for rel in graph.relationships:
            if rel not in code_graph.relationships:
                code_graph.relationships.append(rel)

    return code_graph


def print_graph(code_graph):
    print("Nodes in the code graph:")
    for node_id, node in code_graph.nodes.items():
        print(f"ID: {node_id}, Name: {node.name}, Type: {node.type}, Location: {node.location}")

    print("\nRelationships in the code graph:")
    for rel in code_graph.relationships:
        from_id, to_id, relationship_type = rel
        print(f"From: {from_id}, To: {to_id}, Relationship: {relationship_type}")  
