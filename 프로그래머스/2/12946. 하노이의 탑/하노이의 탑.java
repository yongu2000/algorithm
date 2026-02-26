import java.util.*;

class Solution {
    
    List<int[]> moves = new ArrayList<>();
    
    private void dfs(int n, int start, int end, int mid) {
        if (n == 1) {
            moves.add(new int[]{start, end});
            return;
        }
        
        // 1. n-1개를 출발지(start)에서 경유지(mid)로 옮김 (도착지(end)를 경유지로 활용)
        dfs(n - 1, start, mid, end);
        
        // 2. 가장 큰 원판을 목적지(end)로 옮김
        moves.add(new int[]{start, end});
    
        // 3. 경유지(mid)에 있던 n-1개를 목적지(end)로 옮김 (출발지(start)를 경유지로 활용)
        dfs(n - 1, mid, end, start);
    }
    
    public int[][] solution(int n) {
        
        dfs(n, 1, 3, 2);
        
        int[][] answer = new int[moves.size()][2];
        for (int i = 0; i < moves.size(); i++) {
            answer[i] = moves.get(i);
        }
        return answer;
    }
}