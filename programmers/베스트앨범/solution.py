from collections import defaultdict


def solution(genres, plays):
    answer = []
    
    totPlays = defaultdict(int)
    songPlays = defaultdict(list)
    
    for i in range(len(genres)):
        totPlays[genres[i]] = totPlays.get(genres[i], 0) + plays[i]
        songPlays[genres[i]].append((plays[i], i))
        songPlays[genres[i]].sort(key=lambda x: (-x[0], x[1]))
    
    topTotPlays = []
    
    index = 0
    for time in totPlays.values():
        topTotPlays.append((time, index))
        index += 1
    
    topTotPlays.sort(reverse=True)
    
    allSongs = []
    for songList in songPlays.values():
        allSongs.append(songList)
    
    for _, rank in topTotPlays:
        count = 1
        for bestSong in allSongs[rank]:
            if count > 2:
                break
            answer.append(bestSong[1])
            count += 1
    
    return answer
