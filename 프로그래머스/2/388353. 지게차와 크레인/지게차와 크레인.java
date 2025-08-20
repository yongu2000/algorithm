import java.util.*;

class Solution {
    
    class Node {
        public int x;
        public int y;
        
        public Node (int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    
    private int[] dx = {0, 0, -1, 1};
    private int[] dy = {1, -1, 0, 0};
    private int n, m;
    private int answer;
    
    private String[][] store;
    
    private void craine(String request) {
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (store[i][j].equals(request)) {
                    store[i][j] = "-";
                    answer++;
                }
            }            
        }
        
    }
    
    private void forklift(String request) {
        Set<Node> set = new HashSet<>();
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (store[i][j].equals(request) && bfs(new Node(i, j))) {
                    set.add(new Node(i, j));
                    answer++; 
                }
            }            
        }
        
        set.forEach(node -> store[node.x][node.y] = "-");
    }
    
    private boolean bfs(Node start) {
        boolean[][] visited = new boolean[n][m];
        Deque<Node> queue = new ArrayDeque<>();
        
        queue.addLast(start);
        visited[start.x][start.y] = true;
        while (!queue.isEmpty()) {
            Node node = queue.pollFirst();
            
            for (int i = 0; i < 4; i++) {
                int nx = node.x + dx[i];
                int ny = node.y + dy[i];
                
                if (0 > nx || nx >= n || 0 > ny || ny >= m) {
                    return true;
                }
                
                if (0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny] && store[nx][ny] == "-") {
                    visited[nx][ny] = true;
                    queue.addLast(new Node(nx, ny));
                }
            }
        }
        return false;
    }
    
    
    public int solution(String[] storage, String[] requests) {
        answer = 0;
        n = storage.length;
        m = storage[0].length();
        
        store = new String[n][m];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                store[i][j] = String.valueOf(storage[i].charAt(j));
            }            
        }
        
        for (String request : requests) {
            if (request.length() == 2) {
                craine(request.substring(0, 1));
            } else {
                forklift(request);
            }
        }
        
        return n*m - answer;
    }
}