def get_milisecond(time):
    hour_text, minute_text, second_text = time.split(":")
    
    hour = int(hour_text) * 60 * 60 * 1000
    minute = int(minute_text) * 60 * 1000
    second = int(second_text.split(".")[0]) * 1000
    milisecond = int(second_text.split(".")[1])
    
    return hour + minute + second + milisecond

def solution(lines):
    answer = 0
    
    log_dates = []
    for line in lines:
        day, time, processed_time = line.split(" ")
        
        milisecond = get_milisecond(time)
        processed_time = int(float(processed_time[:-1]) * 1000)
        
        log_dates.append((milisecond - processed_time + 1, milisecond))
    
    for index, log_date in enumerate(log_dates):
        throughput = 1
        throughput_end_time = log_date[1] + 1000 - 1
        
        for search_index in range(index + 1, len(log_dates)):
            if throughput_end_time >= log_dates[search_index][0]:
                throughput += 1
        
        answer = max(answer, throughput)
        
    return answer