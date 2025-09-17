import java.util.*;
import java.lang.*;
import java.io.*;

class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(reader.readLine());
        
        int[][] board = new int[n][n];
        
        for (int i = 0; i < n; i++) {
            int[] arr = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            board[i] = arr;
        }

        long[][] dp = new long[n][n];
        dp[0][0] = 1;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int val = board[i][j];

                if (val == 0) break;

                if (val + i < n) dp[val + i][j] += dp[i][j];
                if (val + j < n) dp[i][val + j] += dp[i][j];                
            }
        }

        writer.append(Long.toString(dp[n-1][n-1])).flush();
    }
}