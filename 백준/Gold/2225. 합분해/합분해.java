import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    
    static int MOD = 1000000000;
    
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int[] input = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int n = input[0];
        int k = input[1];
        
        int[][] dp = new int[n+1][k+1];

        for(int i = 0; i <= n; i++){
            dp[i][0] = 0;
            dp[i][1] = 1;
        }
        

        for(int i = 0; i <= k; i++){
            dp[1][i] = i;
        }

        for(int i = 2; i <= n; i++){
            for(int j = 2; j <= k; j++){
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD;
            }
        }

        writer.append(Integer.toString(dp[n][k])).flush();
    }
}