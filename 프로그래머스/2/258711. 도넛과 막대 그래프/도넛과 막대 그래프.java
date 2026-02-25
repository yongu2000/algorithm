import java.util.*;

class Solution {
    public int[] solution(int[][] edges) {
        int INF = 1_000_001;
        List<List<Integer>> graph = new ArrayList<>();
        
        for (int i = 0; i < INF; i++) {
            graph.add(new ArrayList<>());
        }
        
        int maxEdge = -1;
        for (int[] edge : edges) {
            int start = edge[0];
            int end = edge[1];
            
            maxEdge = Math.max(start, Math.max(end, maxEdge));
            
            graph.get(start).add(end);
        }
        
        // 2개 이상 있는 것 중 루프가 없는 것이 생성한 정점
        Set<Integer> candidates = new HashSet<>();
        for (int i = 1; i < graph.size(); i++) {
            if (graph.get(i).size() >= 2) candidates.add(i);
        }

        int plusNode = -1;
        
        for (Integer candidate : candidates) {
            Deque<Integer> queue = new ArrayDeque<>();
            boolean[] visited = new boolean[INF];
            queue.add(candidate);
            
            boolean isPlusNode = true;
            
            while (!queue.isEmpty()) {
                int cur = queue.pollFirst();
                visited[cur] = true;
                for (int next : graph.get(cur)) {
                    if (visited[next] && next == candidate) {
                        isPlusNode = false;
                        break;
                    }
                    if (!visited[next]) queue.add(next);
                }
            }
            
            if (isPlusNode) plusNode = candidate;
        }
        
        
        int totalGraph = graph.get(plusNode).size();
        int doughnutGraph = 0;
        int eightGraph = 0;
        int stickGraph = 0;
        
        boolean[] visited = new boolean[maxEdge+1];
        int[] visitedCount = new int[maxEdge+1];
        
        for (int i = 1; i <= maxEdge; i++) {
            if (i == plusNode) continue;
            if (visited[i]) continue;
            Deque<Integer> queue = new ArrayDeque<>();
            queue.add(i);
            
            boolean isDoughnut = false;
            boolean isEight = false;
            
            while (!queue.isEmpty()) {
                int cur = queue.pollFirst();
                visited[cur] = true;
                if (graph.get(cur).size() == 2) isEight = true;
                for (int next : graph.get(cur)) {
                    if (visited[next] && next == i) isDoughnut = true;
                    if (!visited[next]) queue.add(next);
                }
            }
            

            if (isEight) {
                eightGraph++;
                continue;
            }
            if (isDoughnut) doughnutGraph++;
            
        }
        
        stickGraph = totalGraph - doughnutGraph - eightGraph;

        int[] answer = {plusNode, doughnutGraph, stickGraph, eightGraph};
        return answer;
    }
}