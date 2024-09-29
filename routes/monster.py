import logging

from flask import jsonify, request
from routes import app

logger = logging.getLogger(__name__)


@app.route("/efficient-hunter-kazuma", methods=["POST"])
def main():
    data = request.get_json()
    efficiencies = []
    for item in data:
        time_frames = item["monsters"]
        efficiency = find_max_efficiency(time_frames)
        efficiencies.append(efficiency)
    output = [{"efficiency": n} for n in efficiencies]
    return jsonify(output)


def find_max_efficiency(time_frames):
    n = len(time_frames)
    # Initialize dp arrays for 3 states: rest, attack, and circle
    rest = [0] * (n + 1)
    attack = [0] * (n + 1)
    circle = [0] * (n + 1)

    # Dynamic Programming base cases:
    rest[0] = 0  # Starting with rest, no penalty or points
    attack[0] = float("-inf")  # Can't start with attack
    circle[0] = -time_frames[0]  # Can't start with circle

    # Iterate over the time frames
    for i in range(1, n):
        monsters = time_frames[i]

        # If we rest, we come from either attack or rest
        rest[i] = max(rest[i - 1], attack[i - 1], circle[i - 1])

        # If we attack, we must have come from a circle with mana
        attack[i] = monsters + max(circle[i - 1], rest[i - 1])
        # If we enter a circle, it must come from rest or attack, not another circle
        circle[i] = max(rest[i - 1] - monsters)

    # The answer is the maximum efficiency at the last time frame
    return max(rest[n], attack[n])


# def main():
#     data = request.get_json()
#     efficiency = []
#     for item in data:
#         time_frames = item["monsters"]
#         tree = Tree(time_frames)
#         efficiency.append(tree.find_max(tree.mainNode))
#     output = [{"efficiency": n} for n in efficiency]
#     return jsonify(output)
#
#
# class Node:
#     has_mana = False
#     node_cost = 0
#     node_type = "null"
#     right = left = middle = None
#
#     def __init__(self, node_cost, node_type, has_mana):
#         self.has_mana = has_mana
#         self.node_cost = node_cost
#         self.node_type = node_type
#
#     def set_right(self, right):
#         self.right = right
#
#     def set_middle(self, middle):
#         self.middle = middle
#
#     def set_left(self, left):
#         self.left = left
#
#
# class Tree:
#     mainNode = Node(0, "null", False)
#
#     def __init__(self, time_frames):
#         self.populate_tree(time_frames)
#
#     def populate_tree(self, time_frames):
#         current_parent_nodes = [self.mainNode]
#         next_parent_nodes = []
#         for i in range(len(time_frames)):
#             for node in current_parent_nodes:
#                 if node.node_type == "null":
#                     node.set_middle(Node(0, "rest", False))
#                     node.set_right(Node(-time_frames[i], "circle", True))
#                 elif node.node_type == "rest":
#                     node.set_left(Node(0, "rest", node.has_mana))
#                     if node.has_mana:
#                         node.set_middle(Node(time_frames[i], "attack", False))
#                     else:
#                         node.set_right(Node(-time_frames[i], "circle", True))
#                 elif node.node_type == "attack":
#                     node.set_middle(Node(0, "rest", False))
#                 elif node.node_type == "circle":
#                     node.set_left(Node(time_frames[i], "attack", False))
#                     node.set_right(Node(0, "rest", True))
#
#                 if node.left:
#                     next_parent_nodes.append(node.left)
#                 if node.middle:
#                     next_parent_nodes.append(node.middle)
#                 if node.right:
#                     next_parent_nodes.append(node.right)
#
#             current_parent_nodes = next_parent_nodes
#             next_parent_nodes = []
#
#     def find_max(self, node):
#
#         if node.middle == None and node.left == None and node.right == None:
#             return node.node_cost
#
#         if node.right != None:
#             right_cost = self.find_max(node.right)
#             print("Right: " + str(right_cost))
#         else:
#             right_cost = 0
#         if node.left != None:
#             left_cost = self.find_max(node.left)
#             print("Left: " + str(left_cost))
#         else:
#             left_cost = 0
#         if node.middle != None:
#             middle_cost = self.find_max(node.middle)
#             print("Middle: " + str(middle_cost))
#         else:
#             middle_cost = 0
#
#         node.node_cost += max(right_cost, left_cost, middle_cost)
#         return node.node_cost
#

