import java.util.*;
import java.time.*;

class LogDate {
    int start;
    int end;
    
    LogDate(int start, int end) {
        this.start = start;
        this.end = end;
    }
}

class Solution {
    public static int getMilisecond(String time) {
        String[] timeArray = time.split(":");
        int hour = Integer.parseInt(timeArray[0]) * 60 * 60 * 1000;
        int minute = Integer.parseInt(timeArray[1]) * 60 * 1000;
        int second = Integer.parseInt(timeArray[2].split("\\.")[0]) * 1000;
        int milisecond = Integer.parseInt(timeArray[2].split("\\.")[1]);
        
        return hour + minute + second + milisecond;
    }
    
    public int solution(String[] lines) {
        int answer = 0;
        
        ArrayList<LogDate> logDates = new ArrayList<>();
        for (String line : lines) {
            String[] log = line.split(" ");
            String time = log[1];
            int processedTime = (int) (Double.parseDouble(log[2].replace("s", "")) * 1000);
            int milisecond = getMilisecond(time);
            
            logDates.add(new LogDate(milisecond - processedTime + 1, milisecond));
        }
        
        int logIndex = 0;
        for (LogDate logDate : logDates) {
            int searchLogIndex = logIndex + 1;
            int throughputSecond = logDate.end + 1000 - 1;
            int throughput = 1;
            
            while (searchLogIndex < logDates.size()) {
                if (throughputSecond >= logDates.get(searchLogIndex).start) {
                    throughput++;
                }
                
                searchLogIndex++;
            }
            
            answer = Math.max(answer, throughput);
            logIndex++;
        }
        
        return answer;
    }
}