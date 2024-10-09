from entities.CodeGraph import CodeGraph
from entities.CodeNode import CodeNode

def parse_ast(ast_json, file_path):
    graph = CodeGraph()

    file_location = [file_path]
    
    def traverse(node, parent_id=None):
        if not isinstance(node, dict) or 'type' not in node:
            return None

        name = get_node_name(node)
        location = f"{node.get('loc', {}).get('start', {}).get('line', 0)}:{node.get('loc', {}).get('start', {}).get('column', 0)}"
        code_node = CodeNode(node['type'], name, location, file_location[0])
        code_node = graph.add_node(code_node)  # This will either add the node or return an existing one
        current_id = code_node.id
        
        if parent_id:
            # Only add 'contains' for specific parent-child relationships
            if node['type'] not in ['MemberExpression', 'CallExpression']:
                graph.add_relationship(parent_id, current_id, 'contains')
        
        if node['type'] == 'CallExpression':
            if 'callee' in node:
                callee_node = traverse(node['callee'], current_id)
                if callee_node:
                    graph.add_relationship(current_id, callee_node.id, 'calls')
        
        elif node['type'] == 'MemberExpression':
            object_node = traverse(node['object'], current_id)
            property_node = traverse(node['property'], current_id)
            if object_node:
                graph.add_relationship(current_id, object_node.id, 'accesses')
            if property_node:
                graph.add_relationship(current_id, property_node.id, 'property')
        
        elif node['type'] in ['ClassDeclaration', 'ClassExpression']:
            if 'superClass' in node and node['superClass']:
                super_class_node = traverse(node['superClass'], current_id)
                if super_class_node:
                    graph.add_relationship(current_id, super_class_node.id, 'extends')
        
        for key, value in node.items():
            if key in ['callee', 'object', 'property', 'superClass']:
                continue  # These are already handled above
            if isinstance(value, dict):
                child_node = traverse(value, current_id)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        child_node = traverse(item, current_id)
        
        return code_node
    
    traverse(ast_json)
    return graph

def get_node_name(node):
    if node.get('id') and node['id'].get('name'):
        return node['id']['name']
    elif node.get('name'):
        return node['name']
    elif node.get('value') is not None and type(node.get('value')) == dict:
        return f"{node['type']}_{node['value'].get('name')}"
    elif node.get('value') is not None:
         return f"{node['type']}_{node['value']}"
    else:
        return f"{node['type']}_{node.get('kind', '')}"

def validate_relationships(graph):
    relationship_dict = {}
    for from_id, to_id, rel_type in graph.relationships:
        if (to_id, from_id, rel_type) in relationship_dict:
            print(f"Warning: Circular reference detected between {from_id} and {to_id}")
        relationship_dict[(from_id, to_id, rel_type)] = True
