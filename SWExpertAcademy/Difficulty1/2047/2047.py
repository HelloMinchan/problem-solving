str = input()
for ch in str:
    if ch == '_' or ch == '.':
        print(ch, end = '')
    else:
        if ord(ch) >= 65 and ord(ch) <= 90:
            print(ch, end = '')
        else:
            print(chr(ord(ch)-32), end = '')
