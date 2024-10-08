import json

# Function to read and parse the AST JSON file
def read_ast_json(file_path):
    """
    This code defines a function that takes a path to a JSON file,
    reads the content of the file, and parses it into a dictionary,
    where keys are file paths and values are the corresponding AST objects.

    Example usage:
    - ast_data = read_ast_json('path/to/ast.json')
    """
    with open(file_path, 'r') as file:
        # Load the stringified JSON data
        data = json.load(file)
        # Convert the list of file paths and AST strings into a dictionary
        ast_dict = {entry[0]: json.loads(entry[1]) for entry in data}
    return ast_dict
