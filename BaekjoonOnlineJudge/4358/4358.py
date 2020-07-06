import sys
input = sys.stdin.readline


class Node():

    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = dict()


while 1:
    name = input().rstrip()

    if name == "":
        break

    
