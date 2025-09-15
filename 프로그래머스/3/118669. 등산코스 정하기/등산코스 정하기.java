import java.util.*;

class Solution {
    
    List<List<int[]>> graph;
    Set<Integer> summitsSet;
    
    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        int[] answer = new int[2];
        graph = new ArrayList<>();
        
        Arrays.sort(summits);
        Arrays.sort(gates);
        
        for (int i = 0; i <= n; i++) graph.add(new ArrayList<>());
        
        summitsSet = new HashSet<>();
        for (int s : summits) summitsSet.add(s);
        
        for (int[] path : paths) {
            int start = path[0];
            int end = path[1];
            int val = path[2];
            
            graph.get(start).add(new int[]{end, val});
            graph.get(end).add(new int[]{start, val});
        }
        
        int[] dist = new int[n+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        
        for (int gate : gates) {
            dist[gate] = 0;
            pq.add(new int[]{gate, 0});
        }
        
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int node = cur[0];
            int cost = cur[1];
            
            if (cost > dist[node]) continue;
            if (summitsSet.contains(node)) continue; // 서밋 도달 시 더 탐색 안 함
            
            for (int[] next : graph.get(node)) {
                int nx = next[0], w = next[1];
                int newCost = Math.max(cost, w);
                if (dist[nx] > newCost) {
                    dist[nx] = newCost;
                    pq.add(new int[]{nx, newCost});
                }
            }
        }
        
        
        int bestSummit = -1; 
        int bestIntensity = Integer.MAX_VALUE;
        for (int s : summits) {
            if (dist[s] < bestIntensity) {
                bestIntensity = dist[s];
                bestSummit = s;
            }
        }
        
        
        return new int[]{bestSummit, bestIntensity};
    }
}