import sys
input = sys.stdin.readline


class Node():

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.children = dict()


class Trie():

    def __init__(self):
        self.head = Node(None, None)
    
    def insert(self, string):
        curr_node = self.head
        
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char, None)
            
            curr_node = curr_node.children[char]
        
        curr_node.data = string
    
    def search(self, string):
        curr_node = self.head
        
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        
        if curr_node.data != None:
            return True
        

N, M = map(int, input().split())

saveWords = [input().rstrip() for _ in range(N)]
searchWords = [input().rstrip() for _ in range(M)]

trie = Trie()

for word in saveWords:
    trie.insert(word)

answer = 0
for word in searchWords:
    if trie.search(word):
        answer += 1

print(answer)
