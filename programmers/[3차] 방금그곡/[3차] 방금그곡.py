# 멜로디에서 '#' 제거
def transMelody(string):
    string = string.replace("C#", 'c')
    string = string.replace("D#", 'd')
    string = string.replace("F#", 'f')
    string = string.replace("G#", 'g')
    string = string.replace("A#", 'a')
    
    return string

    
def solution(m, musicinfos):
    answer_song = ""
    answer_melody = ""
    
    melody_hash = dict()
    
    m = transMelody(m)
    
    for i in range(len(musicinfos)):
        begin, end, song, melody = musicinfos[i].split(',')
        
        melody = transMelody(melody)
        
        hour1 = int(begin.split(':')[0])
        min1 = int(begin.split(':')[1])
        hour2 = int(end.split(':')[0])
        min2 = int(end.split(':')[1])
        
        # 라디오에서 재생된 시간
        totalMin = (hour2 - hour1) * 60 + (min2 - min1)
        
        # 라디오에서 흘러나온 멜로디
        melody = melody * (totalMin // len(melody)) + melody[:totalMin % len(melody)]
        
        # 라디오에 멜로디가 존재한다면
        if m in melody:
            # 재생된 시간이 제일 긴 제목 반환 조건
            if len(answer_melody) < len(melody):
                answer_song = song
                answer_melody = melody
            
    # 조건이 일치하는 음악이 없을 경우
    if answer_song == "":
        return "(None)"
    
    return answer_song
