import sys

input = sys.stdin.readline

N = int(input())
people = []
for _ in range(N):
    people.append(tuple(map(int, input().split())))

answer = []

for target_person in range(N):
    bigger_person_count = 0
    for compare_person in range(N):
        if target_person == compare_person:
            continue
        else:
            if (
                people[target_person][0] < people[compare_person][0]
                and people[target_person][1] < people[compare_person][1]
            ):
                bigger_person_count += 1

    answer.append(bigger_person_count + 1)
else:
    print(*answer)
