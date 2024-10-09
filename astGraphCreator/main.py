import sys
import argparse

from astReader.astReader import read_ast_json
from entities.CodeGraph import CodeGraph
from astParser import parse_ast
from astParser import validate_relationships

def main():

    # astJSON_StringifiedFilePath = 

    # if len(sys.argv) < 2:
    #     print("Provide the path to the Stringified AST Json file along with the run command")
    #     print("Example: python main.py .../path/to/file.json")
    #     return

    # Read and parse the AST JSON file
    ast_dict = read_ast_json("/Users/dhruvparthasarathy/Documents/personal/cli-gen/experiments/sample.json")

    # Process the parsed AST data into a graph structure
    code_graph = CodeGraph()

    for file_path, ast_json in ast_dict.items():
        graph = parse_ast(ast_json)
        code_graph.nodes.update(graph.nodes)
        for rel in graph.relationships:
            if rel not in code_graph.relationships:
                code_graph.relationships.append(rel)

    def print_graph(code_graph):
        print("Nodes in the code graph:")
        for node_id, node in code_graph.nodes.items():
            print(f"ID: {node_id}, Name: {node.name}, Type: {node.type}, Location: {node.location}")

        print("\nRelationships in the code graph:")
        for rel in code_graph.relationships:
            from_id, to_id, relationship_type = rel
            print(f"From: {from_id}, To: {to_id}, Relationship: {relationship_type}")        

    print_graph(code_graph)

    # Use this after generating the graph
    validate_relationships(code_graph)    

if __name__ == "__main__":
    main()
