import java.util.*;

class Location {
    int move;
    int i;
    int j;
    
    Location(int move, int i, int j) {
        this.move = move;
        this.i = i;
        this.j = j;
    }
}

class Solution {
    private static final int MAXIMUM_LENGTH = 102;
    private static int[][] map = new int[MAXIMUM_LENGTH][MAXIMUM_LENGTH];
    private static boolean visit[][] = new boolean[MAXIMUM_LENGTH][MAXIMUM_LENGTH];
    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {-1, 1, 0, 0};
    private static final int WAY_COUNT = 4;
    
    private static void makeMap(int[][] rectangles) {
        for (int[] rectangle : rectangles) {
            int x1 = rectangle[0] * 2;
            int y1 = rectangle[1] * 2;
            int x2 = rectangle[2] * 2;
            int y2 = rectangle[3] * 2;
            
            for (int i = y1; i <= y2; i++) {
                for (int j = x1; j <= x2; j++) {
                    map[i][j] = 1;
                }
            }    
        }
        
        for (int[] rectangle : rectangles) {
            int x1 = rectangle[0] * 2;
            int y1 = rectangle[1] * 2;
            int x2 = rectangle[2] * 2;
            int y2 = rectangle[3] * 2;
            
            for (int i = y1 + 1; i < y2; i++) {
                for (int j = x1 + 1; j < x2; j++) {
                    map[i][j] = 0;
                }
            }
        }
    }
    
    private static int dijkstra(int characterX, int characterY, int itemX, int itemY) {
        int answer = 0;
        PriorityQueue<Location> locationPQ = new PriorityQueue<>((l1, l2) -> l1.move - l2.move);
        visit[characterY][characterX] = true;
        locationPQ.add(new Location(0, characterY, characterX));
        
        while (!locationPQ.isEmpty()) {
            Location currentLocation = locationPQ.poll();
            
            if (currentLocation.i == itemY && currentLocation.j == itemX) {
                return currentLocation.move / 2;
            }
            
            for (int way = 0; way < WAY_COUNT; way++) {
                int nextI = currentLocation.i + dy[way];
                int nextJ = currentLocation.j + dx[way];
                
                
                if (nextI < 0 || nextI > MAXIMUM_LENGTH - 1 || nextJ < 0 || nextJ > MAXIMUM_LENGTH - 1) {
                    continue;
                }
                
                if (!visit[nextI][nextJ] && map[nextI][nextJ] == 1) {
                    visit[nextI][nextJ] = true;
                    locationPQ.add(new Location(currentLocation.move + 1, nextI, nextJ));
                }
            }
        }
        
        return answer;
    }
    
    public int solution(int[][] rectangles, int characterX, int characterY, int itemX, int itemY) {
        int answer = 0;
        
        makeMap(rectangles);
        
        answer = dijkstra(characterX * 2, characterY * 2, itemX * 2, itemY * 2);
        
        return answer;
    }
}