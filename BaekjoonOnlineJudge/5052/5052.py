import sys

input = sys.stdin.readline


class Node:
    def __init__(self, key=None):
        self.key = key
        self.children = dict()


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, phone_number):
        cur_node = self.head

        for number in phone_number:
            if number not in cur_node.children.keys():
                cur_node.children[number] = Node(number)
            cur_node = cur_node.children[number]

        if len(cur_node.children.keys()):
            return True
        else:
            return False


t = int(input())

for _ in range(t):
    trie = Trie()

    n = int(input())

    phone_numbers = []
    for _ in range(n):
        phone_numbers.append(list(input().rstrip()))

    phone_numbers.sort(key=lambda x: -len(x))

    for phone_number in phone_numbers:
        if trie.insert(phone_number):
            print("NO")
            break
    else:
        print("YES")
