from entities.CodeGraph import CodeGraph
from entities.CodeNode import CodeNode

def parse_ast(ast_json):
    graph = CodeGraph()
    
    def traverse(node, parent_id=None):
        if isinstance(node, dict) and 'type' in node:
            name = get_node_name(node)
            location = f"{node.get('loc', {}).get('start', {}).get('line', 0)}:{node.get('loc', {}).get('start', {}).get('column', 0)}"
            code_node = CodeNode(node['type'], name, location)
            graph.add_node(code_node)
            current_id = code_node.id
            
            if parent_id:
                graph.add_relationship(parent_id, current_id, 'contains')
            
            if node['type'] == 'CallExpression':
                if 'callee' in node:
                    callee_name = get_node_name(node['callee'])
                    callee_id = f"CallExpression_{callee_name}"
                    graph.add_relationship(current_id, callee_id, 'calls')
            
            elif node['type'] in ['ClassDeclaration', 'ClassExpression']:
                if 'superClass' in node and node['superClass']:
                    super_class_name = get_node_name(node['superClass'])
                    super_class_id = f"Class_{super_class_name}"
                    graph.add_relationship(current_id, super_class_id, 'extends')
            
            for key, value in node.items():
                if isinstance(value, dict):
                    traverse(value, current_id)
                elif isinstance(value, list):
                    for item in value:
                        traverse(item, current_id)
    
    traverse(ast_json)
    return graph

# def get_node_name(node):
#     if 'type' in node:
#         if node.get('id', {}):
#             return node.get('id', {}).get('name')
#         elif node.get('name'):
#             return node.get('name')
#         else:
#             return node['type']
#     elif 'value' in node:
#         return f"{node['type']}_{node['value']}"
#     else:
#         return f"Unnamed_{node.get('type', 'Node')}"

def get_node_name(node):
    if node.get('id') and node['id'].get('name'):
        return node['id']['name']
    elif node.get('name'):
        return node['name']
    elif node.get('value') is not None:
        return f"{node['type']}_{node['value']}"
    else:
        return f"{node['type']}_{node.get('kind', '')}"
