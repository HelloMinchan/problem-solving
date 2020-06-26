import sys
input = sys.stdin.readline


def pisano():
    back2 = 0
    back1 = 0
    now = 1

    while 1:
        back2 = back1
        back1 = now
        now = (back1 + back2) % 1000000

        sequence.append(now)

        if back1 == 0 and now == 1:
            sequence.pop()
            sequence.pop()
            break


n = int(input())

sequence = [0, 1]

pisano()

print(sequence[n % len(sequence)])
