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

    def printStructure(self, L, curr_node):
        if L == 0:
            curr_node = self.head
        
        for child in sorted(curr_node.children.keys()):
            print("--" * L, child, sep="")
            self.printStructure(L + 1, curr_node.children[child])

        
trie = Trie()

N = int(input())

for _ in range(N):
    temp = list(input().split())
    trie.insert(temp[1:])

trie.printStructure(0, None)
