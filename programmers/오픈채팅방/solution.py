def solution(record):
    answer = []
    
    hash_name = dict()
    
    for line in record:
        line = line.split()
        
        if line[0] == "Enter" or line[0] == "Change":
            hash_name[line[1]] = line[2]
    
    for line in record:
        line = line.split()
        
        if line[0] == "Enter":
            answer.append(hash_name[line[1]] + "님이 들어왔습니다.")
        elif line[0] == "Leave":
            answer.append(hash_name[line[1]] + "님이 나갔습니다.")
    
    return answer
