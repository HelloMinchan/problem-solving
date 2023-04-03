import sys

sys.setrecursionlimit(10**7)


class Node:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right


def preorder(node):
    if node is None:
        return

    preorder_list.append(node.info[2])
    preorder(node.left)
    preorder(node.right)


def postorder(node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    postorder_list.append(node.info[2])


def solution(nodeinfo):
    global preorder_list, postorder_list
    preorder_list = []
    postorder_list = []

    new_nodeinfo = [
        (node[0], node[1], index + 1) for index, node in enumerate(nodeinfo)
    ]
    new_nodeinfo.sort(key=lambda node: (-node[1], node[0]))

    root = Node(new_nodeinfo[0])

    for child_node in new_nodeinfo[1:]:
        cur_node = root

        while True:
            if child_node[0] < cur_node.info[0]:
                if cur_node.left:
                    cur_node = cur_node.left
                    continue
                else:
                    cur_node.left = Node(child_node)
                    break
            if child_node[0] > cur_node.info[0]:
                if cur_node.right:
                    cur_node = cur_node.right
                    continue
                else:
                    cur_node.right = Node(child_node)
                    break

    preorder(root)
    postorder(root)

    return [preorder_list, postorder_list]
