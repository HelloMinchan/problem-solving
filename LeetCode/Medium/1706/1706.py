# 3:20 ~ 3:48


def drop_the_ball(grid, i, j):
    bottom = len(grid)
    left_wall = -1
    right_wall = len(grid[0])
    # 방향 위->아래 : "down", 왼->오 : right, "오->왼" : "left"
    way = "down"

    while True:
        # 밑 바닥으로 떨어진 경우
        if i == bottom:
            return j

        # 양옆 벽에 막힌 경우
        if j in [left_wall, right_wall]:
            return -1

        # 이동 시작
        if way == "down":
            if grid[i][j] == 1:
                j += 1
                way = "right"
            else:
                j -= 1
                way = "left"
        elif way == "right":
            if grid[i][j] == 1:
                i += 1
                way = "down"
            else:
                return -1
        else:
            if grid[i][j] == 1:
                return -1
            else:
                i += 1
                way = "down"


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        answer = []

        for j in range(len(grid[0])):
            answer.append(drop_the_ball(grid, 0, j))

        return answer
