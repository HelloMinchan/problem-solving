import sys
input = sys.stdin.readline

word = input().rstrip()
tot = len(list(word))

case1 = word.count("z=")
case2 = word.count("dz=")
case3 = word.count("c=")
case4 = word.count("c-")
case5 = word.count("d-")
case6 = word.count("lj")
case7 = word.count("nj")
case8 = word.count("s=")

if case1 > 0:
    if case2 > 0:
        tot -= (case1 - case2) + case2 * 2
if case3 > 0:
    tot -= case3
if case4 > 0:
    tot -= case4
if case5 > 0:
    tot -= case5
if case6 > 0:
    tot -= case6
if case7 > 0:
    tot -= case7
if case8 > 0:
    tot -= case8

print(tot)