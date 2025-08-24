import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        
        Arrays.sort(targets, (a, b) -> {
            if (a[1] == b[1]) {
                return Integer.compare(a[0], b[0]);
            }
            return Integer.compare(a[1], b[1]);
            });
        
        int max = -1;
        for (int[] target : targets) {
            int start = target[0] + 1;
            int end = target[1];
            
            if (start > max) {
                answer++;
                max = Math.max(max, end);
            }
            
        }
        return answer;
    }
}