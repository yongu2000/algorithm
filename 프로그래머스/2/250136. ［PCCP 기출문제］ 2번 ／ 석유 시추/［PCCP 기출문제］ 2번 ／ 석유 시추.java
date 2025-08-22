import java.util.*;

class Solution {
    
    class Node {
        int x, y;
        Node(int x, int y) { this.x = x; this.y = y; }
                @Override
        public String toString() {
            return "(" + x + ", " + y + ")";
        }
    }

    private int[] dx = {0, 0, 1, -1};
    private int[] dy = {1, -1, 0, 0};
        
    private boolean[][] visited;
    private int n, m;
    
    private void bfs(int x, int y, int[][] land, int[] colSum) {
        Deque<Node> queue = new ArrayDeque<>();
        queue.add(new Node(x, y));
        visited[x][y] = true;

        
        int size = 0;
        Set<Integer> temp = new HashSet<>();
        
        
        while (!queue.isEmpty()) {
            Node node = queue.pollFirst();
            size++;
            temp.add(node.y);
            
            for (int i = 0; i < 4; i++) {
                int nx = node.x + dx[i];
                int ny = node.y + dy[i];
                
                if (0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny] && land[nx][ny] == 1) {
                    visited[nx][ny] = true;      
                    queue.add(new Node(nx, ny));
                }
                    
            }
        }
        
        for (int t : temp) {
            colSum[t] += size;
        }
        
    }
    
    public int solution(int[][] land) {
        int answer = 0;
        
        n = land.length;
        m = land[0].length;
        visited = new boolean[n][m];
        
        int[] colSum = new int[m];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (land[i][j] == 1 && !visited[i][j]) {
                    bfs(i, j, land, colSum);
                }
            }
        }
        
        for (int val : colSum) {
            answer = Math.max(val, answer);
        }
        return answer;
    }
}