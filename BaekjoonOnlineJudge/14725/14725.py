import sys
input = sys.stdin.readline


class Node():

    def __init__(self, key):
        self.key = key
        self.children = dict()


class Trie():

    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]

    def search(self, L):
        curr_node = self.head

        print("--" * L, end="")

        
trie = Trie()
