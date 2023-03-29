from collections import defaultdict
import sys

input = sys.stdin.readline

A = int(input())
T = int(input())
answer = int(input())

seq = [0, 1, 0, 1, 0, 1]

target_count = defaultdict(int)

cycle = 2
person = 0

while True:
    for index, target in enumerate(seq):
        if index in [4, 5]:
            for _ in range(cycle):
                target_count[target] += 1

                if target_count[target] == T and target == answer:
                    print(person)
                    sys.exit(0)

                person = (person + 1) % A
        else:
            target_count[target] += 1

            if target_count[target] == T and target == answer:
                print(person)
                sys.exit(0)

            person = (person + 1) % A

    cycle += 1
