def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[i])):
            presentLand = land[i][j]
            for k in range(len(land[i - 1])):
                if land[i][j] < presentLand + land[i - 1][k] and j != k:
                    land[i][j] = presentLand + land[i - 1][k]
                    
    return max(land[-1])
