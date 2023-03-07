from collections import defaultdict
import sys

input = sys.stdin.readline

g, s = map(int, input().split())
W = input().rstrip()
S = input().rstrip()

maya_word = defaultdict(int)
for spell in W:
    maya_word[spell] += 1

answer = 0
left = 0
right = 0

window = defaultdict(int)
while right <= s:
    if right - left == g:
        if maya_word == window:
            answer += 1

        window[S[left]] -= 1
        if window[S[left]] == 0:
            del window[S[left]]
        left += 1
    else:
        if right < s:
            window[S[right]] += 1
        right += 1

print(answer)
