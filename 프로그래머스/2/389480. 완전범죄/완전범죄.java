import java.util.Arrays;

class Solution {
    public int solution(int[][] info, int n, int m) {
        int len = info.length;
        int INF = Integer.MAX_VALUE;
        
        int[][] dp = new int[len+1][m];
        
        for (int[] d : dp) Arrays.fill(d, INF);
        
        dp[0][0] = 0;
        
        for (int i = 1; i <= len; i++) {
            int aTrace = info[i - 1][0];
            int bTrace = info[i - 1][1];
            
            for (int j = 0; j < m; j++) {
                if (dp[i - 1][j] == INF) continue;
                if (dp[i - 1][j] + aTrace < n) dp[i][j] = Math.min(dp[i][j], dp[i - 1][j] + aTrace);
                if (j + bTrace < m) dp[i][j + bTrace] = Math.min(dp[i][j + bTrace], dp[i - 1][j]);
            }
        }

        int answer = INF;
        
        for (int j = 0; j < m; j++) answer = Math.min(answer, dp[len][j]);
       
        return (answer == INF) ? -1 : answer;

    }
}