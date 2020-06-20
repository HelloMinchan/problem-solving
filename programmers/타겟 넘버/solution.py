def solution(numbers, target):
    tree = [0]
    for num in numbers:
        subTree = []
        for node in tree:
            subTree.append(node + num)
            subTree.append(node - num)
        tree = subTree
        
    return tree.count(target)
