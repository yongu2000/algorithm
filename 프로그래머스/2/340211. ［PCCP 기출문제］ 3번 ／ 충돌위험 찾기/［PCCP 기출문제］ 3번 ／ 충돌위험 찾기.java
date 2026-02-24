import java.util.*;

class Solution {
    
    private class Point {
        public int x;
        public int y;
        
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
        
        @Override
        public boolean equals(Object o) {
            if (this == o)
                return true;
            if (!(o instanceof Point))
                return false;
            Point point = (Point)o;
            return x == point.x && y == point.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
        
        public String toString() {
            return "[" + x + ", " + y + "]";
        }
    }
    
    private void record(Map<Integer, Map<String, Integer>> result, int time, Point current) {
        Map<String, Integer> temp = result.getOrDefault(time, new HashMap<String, Integer>());
        temp.put(current.toString(), temp.getOrDefault(current.toString(), 0) + 1);
        result.put(time, temp);
    }
    
    public int solution(int[][] points, int[][] routes) {
        int answer = 0;
        
        Map<Integer, Map<String, Integer>> result = new HashMap<>();
        
        for (int[] route : routes) {
            int time = 0;
            
            int start = route[0] - 1;
            Point current = new Point(points[start][0], points[start][1]);

            record(result, time++, current);
                
            for (int i = 1 ; i < route.length; i++) {
                int end = route[i] - 1; 
                Point destination = new Point(points[end][0], points[end][1]);
                
                while (!current.equals(destination)) {
                    if (current.x != destination.x) {
                        if (current.x < destination.x) current.x++;
                        else current.x--;
                    }
                    else if (current.y != destination.y) {
                        if (current.y < destination.y) current.y++;
                        else current.y--;
                    }
                    
                    record(result, time++, current);
                }
            }
        }
        
        for (Map<String, Integer> point : result.values()) {
            for (Integer value : point.values()) {
                if (value >= 2) answer++;
            }
        }
        
        return answer;
    }
}