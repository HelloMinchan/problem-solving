from collections import defaultdict
import sys

input = sys.stdin.readline


def floydwarshall():
    for member3 in range(1, N + 1):
        for member1 in range(1, N + 1):
            for member2 in range(1, N + 1):
                if (
                    adj_matrix[member1][member3] != INF
                    and adj_matrix[member3][member2] != INF
                ):
                    adj_matrix[member1][member2] = min(
                        adj_matrix[member1][member2],
                        adj_matrix[member1][member3] + adj_matrix[member3][member2],
                    )


N = int(input())

INF = sys.maxsize
adj_matrix = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
for member in range(1, N + 1):
    adj_matrix[member][member] = 0

while True:
    member1, member2 = map(int, input().split())

    if member1 == -1 and member2 == -1:
        break

    adj_matrix[member1][member2] = 1
    adj_matrix[member2][member1] = 1


floydwarshall()

rank_dict = defaultdict(list)
max_rank = INF
for index, row in enumerate(adj_matrix[1:]):
    rank = max([score if score != INF else 0 for score in row[1:]])
    max_rank = min(max_rank, rank)
    rank_dict[rank].append(index + 1)

print(max_rank, len(rank_dict[max_rank]))
print(*sorted(rank_dict[max_rank]))
