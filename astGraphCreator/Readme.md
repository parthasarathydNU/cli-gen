# AST Parser and Knowledge Graph Generator

## Overview

This project is an Abstract Syntax Tree (AST) parser and knowledge graph generator for JavaScript code. It takes JavaScript ASTs in JSON format and converts them into a queryable knowledge graph structure. This tool is designed to facilitate code analysis, understanding complex codebases, and potentially integrating with AI-based code assistance systems.

## Features

- Parses JavaScript ASTs from JSON format
- Generates a knowledge graph representing the code structure
- Captures relationships between different code elements (e.g., function calls, class inheritance)
- Handles multiple files, creating a comprehensive graph of the entire codebase
- Provides a foundation for advanced code analysis and AI-assisted development

## Sample Visuzalization

![2D Representation of Knowledge Graph](./viz/2dGraph.png)

![Interactive Graph](./viz/3dGraph.png)

## How It Works

1. **AST Parsing**: The tool reads ASTs in JSON format, typically generated from JavaScript code using tools like Babel.

2. **Graph Generation**: It converts the AST into a graph structure where:
   - Nodes represent code elements (e.g., functions, classes, variables)
   - Edges represent relationships between these elements (e.g., function calls, inheritance)

3. **Multi-File Support**: The tool can process multiple files, creating a unified graph that represents the entire codebase.

4. **Relationship Mapping**: It identifies and maps various relationships in the code, such as:
   - Function calls
   - Class inheritance
   - Variable usage
   - Module imports/exports

## Key Components

- `CodeNode`: Represents a single node in the graph (e.g., a function, class, or variable).
- `CodeGraph`: The main graph structure that holds all nodes and relationships.
- `parse_ast()`: The core function that traverses the AST and builds the graph.
- `get_node_name()`: Helper function to generate meaningful names for AST nodes.
- `print_graph()`: Utility function to display the generated graph structure.

## Usage

1. Ensure you have a JSON file containing the AST of your JavaScript code.
2. Run the script, providing the path to your AST JSON file:

   ```
   python main.py path/to/your/ast.json
   ```

3. The script will generate a knowledge graph and print out the nodes and relationships.

## Output

The tool provides two main types of output:

1. **Nodes**: Representing individual code elements, including their type, name, and location in the source code.
2. **Relationships**: Showing how different nodes are connected (e.g., which function calls another function).

## Future Enhancements

- Integration with code editors for real-time analysis
- Advanced query capabilities for extracting specific information from the graph
- Visualization of the code structure
- AI-powered code suggestions and refactoring recommendations based on the graph structure

## Requirements

- Python 3.x
- JSON parsing capability (built into Python)

## Contributing

Contributions to enhance the functionality, improve efficiency, or extend the capabilities of this tool are welcome. Please submit pull requests or open issues to discuss potential improvements.

## License

[MIT License](./LICENSE)
