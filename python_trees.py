#!/usr/bin/python3
"""python trees"""

import json
import random


def generate_tree_with_leaves(name, level, max_levels, min_children, max_children):
    """
    Generate a tree structure with leaf nodes having extra data but no children.
    """
    if level >= max_levels:
        # Create a leaf node with extra data
        return {
            "name": f"{name}_leaf",
            "color": random.randint(1, 3),  # Assign a random color
            "extraData": f"Extra data for {name}_leaf",  # Add extra data
        }

    # Create a parent node
    node = {
        "name": f"{name}_level_{level}",
        "color": random.randint(1, 3),  # Assign a random color
        "extraData": f"Extra data for {name}_node",  # Add extra data
        "children": []
    }

    # Randomly decide the number of children for the current node between min and max
    num_children = random.randint(min_children, max_children)

    for _ in range(num_children):
        child_node = generate_tree_with_leaves(node['name'], level + 1, max_levels, min_children, max_children)
        node['children'].append(child_node)

    return node

def filter_branches_by_color_2(node):
    """
    Recursively filters branches that start and end with color 2, allowing intermediate nodes with other colors
    only if they are connecting color 2 nodes.
    """

    # Base case: If the node is a leaf, check if it's color 2
    if not node.get("children", []):
        return node if node["color"] == 2 else None

    # Recursive case: If the node is color 2, process its children
    if node["color"] == 2:
        filtered_children = []
        for child in node["children"]:
            filtered_child = filter_branches_by_color_2(child)
            if filtered_child:
                filtered_children.append(filtered_child)

        # Only include this node if it has valid children or is a leaf with color 2
        if filtered_children:
            return {
                "name": node["name"],
                "color": node["color"],
                "extraData": node["extraData"],
                "children": filtered_children,
            }
        else:
            # If no children are valid, check if it's a leaf with color 2
            return node if not node["children"] else None

    # If node is not color 2, only keep it if it has children that are valid branches starting/ending in color 2
    else:
        filtered_children = []
        for child in node["children"]:
            filtered_child = filter_branches_by_color_2(child)
            if filtered_child:
                filtered_children.append(filtered_child)

        # If any children match the color 2 criteria, return the node as part of the connecting branch
        if filtered_children:
            return {
                "name": node["name"],
                "color": node["color"],
                "extraData": node["extraData"],
                "children": filtered_children,
            }

        return None  # If no children match the criteria, discard this node


def main():
    """main"""

    # Generate the tree
    test_tree = generate_tree_with_leaves("node", 0, 4, 2, 4)
    print(f"{json.dumps(test_tree, indent=2)}")

    filtered_tree = filter_branches_by_color_2(test_tree)
    print(f"{json.dumps(filtered_tree, indent=2)}")


main()
