import sys
input = sys.stdin.readline


class Node():

    def __init__(self, key):
        self.key = key
        self.children = dict()


class Trie():

    def __init__(self):
        self.head = Node(None)
    
    def insert(self, directory):
        curr_node = self.head

        for di in directory:
            if di not in curr_node.children:
                curr_node.children[di] = Node(di)
            curr_node = curr_node.children[di]
    
    def printStructure(self, L, curr_node):
        if L == 0:
            curr_node = self.head
        
        for di in sorted(curr_node.children.keys()):
            print(" " * L, di, sep="")
            self.printStructure(L + 1, curr_node.children[di])


trie = Trie()

N = int(input())

for _ in range(N):
    directory = list(input().rstrip().split("\\"))
    
    trie.insert(directory)

trie.printStructure(0, None)
