import java.util.*;

class Solution {
    public int solution(String arr[]) {
        int answer = -1;
        List<Integer> nums = new ArrayList<>();
        List<String> operands = new ArrayList<>();
        
        for (String str : arr) {
            if (str.matches("\\d+")) nums.add(Integer.parseInt(str));
            else operands.add(str);
        }
        
        int n = nums.size();
        
        int[][] maxDp = new int[n][n];
        int[][] minDp = new int[n][n];
        
        for (int i = 0; i < n; i++) {
            Arrays.fill(maxDp[i], Integer.MIN_VALUE);
            Arrays.fill(minDp[i], Integer.MAX_VALUE);
        }
      
        for (int step = 0; step < n; step++) {
            for (int i = 0; i < n - step; i++) {
                int j = i + step;
                
                if (step == 0) {
                    maxDp[i][i] = nums.get(i);
                    minDp[i][i] = nums.get(i);
                } else {
                    for (int k = i; k < j; k++) {
                        if (operands.get(k).equals("+")) {
                            maxDp[i][j] = Math.max(maxDp[i][j], maxDp[i][k] + maxDp[k+1][j]);
                            minDp[i][j] = Math.min(minDp[i][j], minDp[i][k] + minDp[k+1][j]);
                        } else {
                            maxDp[i][j] = Math.max(maxDp[i][j], maxDp[i][k] - minDp[k+1][j]);
                            minDp[i][j] = Math.min(minDp[i][j], minDp[i][k] - maxDp[k+1][j]);
                        }
                    }
                    
                }
                
            }
        }
 
        
        return maxDp[0][n-1];
    }
}