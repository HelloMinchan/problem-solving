import sys
input = sys.stdin.readline

people = [input().split() + [i] for i in range(int(input()))]

for person in sorted(people, key=lambda people: (int(people[0]), people[2])):
    print(person[0], person[1])