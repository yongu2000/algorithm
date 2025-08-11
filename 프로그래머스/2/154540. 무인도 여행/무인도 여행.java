import java.util.*;

class Solution {
    
    static int[] dx = new int[]{0, 0, 1, -1};
    static int[] dy = new int[]{1, -1, 0, 0};
    static boolean[][] visited;
    static int n, m;
    
    class Node {
        public int x;
        public int y;
        
        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    
    private int bfs(String[] maps, int x, int y) {
        int count = 0;
        
        Deque<Node> queue = new ArrayDeque<>();
        visited[x][y] = true;
        queue.addLast(new Node(x, y));
        
        while (!queue.isEmpty()) {
            Node node = queue.pollFirst();
            
            count += Integer.parseInt(String.valueOf(maps[node.x].charAt(node.y)));
            
            for (int i = 0; i < 4; i++) {
                int nx = node.x + dx[i];
                int ny = node.y + dy[i];
                
                if (0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny] && maps[nx].charAt(ny) != 'X') {
                    queue.addLast(new Node(nx, ny));
                    visited[nx][ny] = true;
                }
            }
        }
        
        return count;
    }
    
    public int[] solution(String[] maps) {
        List<Integer> answer = new ArrayList<>();
        
        n = maps.length;
        m = maps[0].length();
        
        visited = new boolean[n][m];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visited[i][j] && maps[i].charAt(j) != 'X') {
                   answer.add(bfs(maps, i, j)); 
                }
            }
        }
        
        Collections.sort(answer);
        
        if (answer.isEmpty()) {
            return new int[]{-1};
        } 
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}