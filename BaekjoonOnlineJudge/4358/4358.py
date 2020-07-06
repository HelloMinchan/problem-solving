import sys
input = sys.stdin.readline


class Node():

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.children = dict()
        self.count = 1


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
            curr_node.count += 1
            return True

        return False
    
    def getCount(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
        
        return curr_node.count
        
            
trie = Trie()
name_list = []
while 1:
    name = input().rstrip()

    if name == "":
        break

    name_list.append(name)

    if trie.search(name):
        continue
    trie.insert(name)

for name in sorted(list(set(name_list))):
    print("%s %.4f" % (name, (trie.getCount(name) / len(name_list)) * 100))
    
