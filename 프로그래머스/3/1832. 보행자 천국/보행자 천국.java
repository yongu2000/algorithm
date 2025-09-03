import java.util.*;

class Solution {
    int MOD = 20170805;
    public int solution(int m, int n, int[][] cityMap) {
        int answer = 0;
        
        int[][] down = new int[m+1][n+1];
        int[][] right = new int[m+1][n+1];
        
        down[1][1] = 1;
        right[1][1] = 1;
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                switch (cityMap[i-1][j-1]) {
                    case 0:
                        down[i][j] += (down[i-1][j] + right[i][j-1]) % MOD;
                        right[i][j] += (down[i-1][j] + right[i][j-1]) % MOD;
                        break;
                    case 1:
                        down[i][j] = 0;
                        right[i][j] = 0;
                        break;
                    case 2:
                        down[i][j] = down[i-1][j];
                        right[i][j] = right[i][j-1];
                        break;
                }
            }
        }
        
        return down[m][n];
    }
}