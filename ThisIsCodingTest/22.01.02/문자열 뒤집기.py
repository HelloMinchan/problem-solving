import sys
input = sys.stdin.readline

S: str = input().rstrip()

answer: int = 0
select_character: str = ""
last_character: str = S[-1]

for target in S:
    if target == last_character:
        select_character = target
        continue
    else:
        if select_character == target:
            continue
        else:
            select_character = target
            answer += 1
            

print(answer)