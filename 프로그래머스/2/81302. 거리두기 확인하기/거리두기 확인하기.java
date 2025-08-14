import java.util.*;

class Solution {
    
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0, 0};
    
    static class Node {
        public int x;
        public int y;
        public int dist;

        public Node(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }
    }
    
    private boolean bfs(int x, int y, String[] place, boolean[][] visited) {
        
        Deque<Node> queue = new ArrayDeque<>();
        visited[x][y] = true;
        queue.addLast(new Node(x, y, 0));
        
        while (!queue.isEmpty()) {
            Node node = queue.pollFirst();
            
            for (int i = 0; i < 4; i++) {
                int nx = node.x + dx[i];
                int ny = node.y + dy[i];
                
                if (0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny] && place[nx].charAt(ny) != 'X') {
                    if (place[nx].charAt(ny) == 'P') {
                        int manhattan = Math.abs(ny - y) + Math.abs(nx - x);
                        System.out.println(nx + " " + ny + " " + x + " " + y);
                        System.out.println(manhattan);
                        
                        if (node.dist+1 <= 2) {
                            return false;
                        } else {
                            visited[nx][ny] = true;
                            queue.addLast(new Node(nx, ny, node.dist+1));
                        }
                        
                    } else {
                        visited[nx][ny] = true;
                        queue.addLast(new Node(nx, ny, node.dist+1));
                    }
                }
            }
        } 
        return true;
        
    }
    
    private int n = 5;
    private int m = 5;
    
    public int[] solution(String[][] places) {
        
        int[] answer = new int[places.length];
        
        for (int i = 0; i < places.length; i++) {
            String[] place = places[i];
            boolean ok = true;
            for (int x = 0; x < n; x++) {
                for (int y = 0; y < m; y++) {
                    if (place[x].charAt(y) == 'P') {
                        boolean[][] visited = new boolean[n][m];
                        ok = true;
                        ok = bfs(x, y, place, visited);                      
                    }
                    if (!ok) {
                        break;
                    }
                }
                if (!ok) {
                    break;
                }
            } 
            if (ok) {
                answer[i] = 1;
            } else {
                answer[i] = 0;
            }
        }
        
        return answer;
    }
}