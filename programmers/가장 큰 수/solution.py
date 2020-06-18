def solution(numbers):
    if not sum(numbers):
        return '0'
    return "".join(sorted(map(str, numbers), reverse=True, key=lambda x: x * 3))
