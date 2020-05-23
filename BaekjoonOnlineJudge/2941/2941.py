import sys
input = sys.stdin.readline

cnt, idx = 0, 0
keyword = [ 'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=' ]

word = input().rstrip()

while idx < len(word):
	if (word[ idx : idx + 3 ] in keyword):
		idx = idx + 3
	elif (word[ idx : idx + 2 ] in keyword):
		idx = idx + 2
	else:
		idx = idx + 1
	cnt = cnt + 1

print(cnt)