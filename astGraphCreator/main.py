import sys
import argparse

from astReader.astReader import read_ast_json
from entities.CodeGraph import CodeGraph
from graphGen.graphUtils import generateGraph


def main():


    if len(sys.argv) < 2:
        print("Provide the path to the Stringified AST Json file along with the run command")
        print("Example: python main.py .../path/to/file.json")
        return

    # Read and parse the AST JSON file
    ast_dict = read_ast_json(sys.argv[1])

    graph = generateGraph(ast_dict)

    print(graph.get_node_ids())


    



if __name__ == "__main__":
    main()
