import java.util.*;

class Solution {
    
    class Node {
        int x, y;
        
        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
        
        @Override
        public boolean equals(Object o) {
            if (o instanceof Node) {
                Node node = (Node) o;
                return node.x == x && node.y == y;
            }
            return false;
        }
        
        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }
    
    // d l r u
    private int[] dx = {1, 0, 0, -1};
    private int[] dy = {0, -1, 1, 0};
    private String[] p = {"d", "l", "r", "u"};
    
    private void dfs(Node curr, Node end, int dist, String path) {
        if (!answer.equals("impossible")) return;
        if (dist == K) {
            if (curr.equals(end)) answer = path;
            return;
        }
        
        int distLeft = K - dist;
        int bestDist = Math.abs(end.x - curr.x) + Math.abs(end.y - curr.y);
        if (distLeft < bestDist) return;
        
        for (int i = 0; i < 4; i++) {
            int nx = curr.x + dx[i];
            int ny = curr.y + dy[i];
            
            if (0 <= nx && nx < N && 0 <= ny && ny < M) {
                dfs(new Node(nx, ny), end, dist+1, path + p[i]);
            }
        }
        return;
    }

    String answer = "impossible";
    int N, M, K;
    
    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        N = n;
        M = m;
        K = k;
        
        int dist = Math.abs(x-r) + Math.abs(y-c);
        if (dist > k) return answer;
        if ((k % 2 == 0 && dist % 2 != 0) || (k % 2 != 0 && dist % 2 == 0)) return answer;
        
        dfs(new Node(x-1, y-1), new Node(r-1, c-1), 0, "");
        
        return answer;
    }
}