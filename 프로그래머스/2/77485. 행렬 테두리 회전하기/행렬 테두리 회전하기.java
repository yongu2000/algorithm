import java.util.*;
class Solution {
    public int[] solution(int rows, int columns, int[][] queries) {
        List<Integer> answer = new ArrayList<>();
        
        int[][] table = new int[rows][columns];
        
        int temp = 1;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                table[i][j] = temp++;
            }
        }
        
        for (int[] query : queries) {
            int x1 = query[0]-1;
            int y1 = query[1]-1;
            int x2 = query[2]-1;
            int y2 = query[3]-1;
            
            int min = 100001;
            
            int init = table[x1][y1];
            min = Math.min(init, min);
            
            for (int i = x1; i < x2; i++) {
                table[i][y1] = table[i+1][y1];
                min = Math.min(table[i][y1], min);
            }
            
            for (int i = y1; i < y2; i++) {
                table[x2][i] = table[x2][i+1];
                min = Math.min(table[x2][i], min);
            }
            
            for (int i = x2; i > x1; i--) {
                table[i][y2] = table[i-1][y2];
                min = Math.min(table[i][y2], min);
            }
            
            for (int i = y2; i > y1; i--) {
                table[x1][i] = table[x1][i-1];
                min = Math.min(table[x1][i], min);
            }
            
            table[x1][y1+1] = init;
            min = Math.min(table[x1][y1+1], min);
            
            answer.add(min);
                                    
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}