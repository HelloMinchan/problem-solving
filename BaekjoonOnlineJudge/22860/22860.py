from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(root):
    cur_name = root.rstrip().split("/")[-1]

    if tree[cur_name]:
        for child_name, child_type in tree[cur_name]:
            # 폴더인 경우
            if child_type == "1":
                file_type, file_count = dfs(f"{root}/{child_name}")

                if not child_count[root].get("file_type", 0):
                    child_count[root]["file_type"] = set()

                if not child_count[root].get("file_count", 0):
                    child_count[root]["file_count"] = 0

                child_count[root]["file_type"] = child_count[root]["file_type"] | file_type
                child_count[root]["file_count"] += file_count

            else:
                if not child_count[root].get("file_type", 0):
                    child_count[root]["file_type"] = set()
                
                if not child_count[root].get("file_count", 0):
                    child_count[root]["file_count"] = 0

                child_count[root]["file_type"].add(child_name)
                child_count[root]["file_count"] += 1

    
    if not child_count[root].get("file_type", 0):
        child_count[root]["file_type"] = set()

    if not child_count[root].get("file_count", 0):
        child_count[root]["file_count"] = 0
        
    return child_count[root]["file_type"], child_count[root]["file_count"]
        

N, M = map(int, input().split())

tree = defaultdict(list)
child_count = defaultdict(dict)

for _ in range(N+M):
    P, F, C = input().split()

    tree[P].append((F,C))

Q = int(input())

dfs("main")

for _ in range(Q):
    path = input().rstrip()

    print(len(child_count[path]["file_type"]), child_count[path]["file_count"])