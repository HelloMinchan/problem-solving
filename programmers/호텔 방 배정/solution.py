import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def find(room, reservedRooms):
    if room not in reservedRooms:
        reservedRooms[room] = room + 1
        return room
    
    reservedRooms[room] = find(reservedRooms[room], reservedRooms)
    return reservedRooms[room]


def solution(k, room_number):
    answer = []
    reservedRooms = dict()
    
    for room in room_number:
        remainedRoom = find(room, reservedRooms)
        answer.append(remainedRoom)
        
    return answer