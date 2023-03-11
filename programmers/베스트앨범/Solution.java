import java.util.*;

class GenreInfo {
    String name;
    int totalPlay;
    
    GenreInfo (String name, int totalPlay) {
        this.name = name;
        this.totalPlay = totalPlay;
    }
}

class MusicInfo {
    int index;
    int play;
    
    MusicInfo (int index, int play) {
        this.index = index;
        this.play = play;
    }
}

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        Map<String, ArrayList<MusicInfo>> musicInfoByGenre = new HashMap<>();
        
        for (int i = 0; i < genres.length; i++) {
            String genre = genres[i];
            int play = plays[i];
            MusicInfo musicInfo = new MusicInfo(i, play);
            
            if (!musicInfoByGenre.containsKey(genre)) {
                musicInfoByGenre.put(genre, new ArrayList<>());
            }
            
            musicInfoByGenre.get(genre).add(musicInfo);
        }
        
        ArrayList<GenreInfo> totalPlayByGenre = new ArrayList<>();
        for (Map.Entry<String, ArrayList<MusicInfo>> e : musicInfoByGenre.entrySet()) {
            int totalPlay = 0;
            for (MusicInfo musicInfo : e.getValue()) {
                totalPlay += musicInfo.play;
            }
            totalPlayByGenre.add(new GenreInfo(e.getKey(), totalPlay));
                                  
            e.getValue().sort((mi1, mi2) -> mi2.play - mi1.play);
        }
        
        totalPlayByGenre.sort((gi1, gi2) -> gi2.totalPlay - gi1.totalPlay);
        for(GenreInfo gi : totalPlayByGenre){
            int musicCount = 0;
            
            for (MusicInfo mi : musicInfoByGenre.get(gi.name)) {
                answer.add(mi.index);
                musicCount++;
                
                if (musicCount == 2) {
                   break;
                }
            }
        }
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}