import java.util.*;

class Solution {
    static class Point {
        private int x;
        private int y;
        
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
        
        @Override
        public String toString() {
            return "[" + x + ", " + y + "]";
        }
        
        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Point)) return false;
            Point other = (Point) o;
            return x == other.x && y == other.y;
        }
        
        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }
    public String[] solution(int[][] line) {        
        Set<Point> set = new HashSet<>();
        int minX = Integer.MAX_VALUE;
        int maxX = Integer.MIN_VALUE;

        int minY = Integer.MAX_VALUE;
        int maxY = Integer.MIN_VALUE;
        
        for (int i = 0; i < line.length-1; i++) {
            for (int j = 1; j < line.length; j++) {
                int a = line[i][0];
                int b = line[i][1];
                int c = line[j][0];
                int d = line[j][1];
                int e = line[i][2];
                int f = line[j][2];
                
                long xNumerator = (long)b * (long)f - (long)e * (long)d;
                long yNumerator = (long)e * (long)c - (long)a * (long)f;
                long denominator = (long)a * (long)d - (long)b * (long)c;
                
                if (denominator == 0 || xNumerator % denominator != 0 || yNumerator % denominator != 0) continue;
                
                int x = (int) (xNumerator / denominator);
                int y = (int) (yNumerator / denominator);
                
                minX = Math.min(minX, x);
                minY = Math.min(minY, y);
                
                maxX = Math.max(maxX, x);
                maxY = Math.max(maxY, y);
                
                set.add(new Point(x, y));
            }
        }
        
        List<String> answer = new ArrayList<>();
        
        StringBuilder sb = new StringBuilder();
        for (int y = maxY; y >= minY; y--) {
            for (int x = minX; x <= maxX; x++) {
                Point p = new Point(x, y);
                if (set.contains(p)) sb.append("*");
                else sb.append(".");
            }
            answer.add(sb.toString());
            sb.setLength(0);
        }
        return answer.toArray(new String[0]);
    }
}