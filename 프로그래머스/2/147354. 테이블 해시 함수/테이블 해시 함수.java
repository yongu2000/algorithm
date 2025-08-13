import java.util.*;

class Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        int answer = 0;
        Arrays.sort(data, (a, b) -> {
            if (a[col-1] == b[col-1]) {
                return Integer.compare(b[0], a[0]);
            }
            return Integer.compare(a[col-1], b[col-1]);
        });
        
        List<Integer> S = new ArrayList<>();
        
        for (int i = row_begin-1; i < row_end; i++) {
            int temp = 0;
            for (int j = 0; j < data[i].length; j++) {
                temp += data[i][j] % (i+1);
            }
            S.add(temp);
        }
        
        answer = S.get(0);
        
        for (int i = 1; i < S.size(); i++) {
            answer = answer ^ S.get(i);
        }
        
        return answer;
    }
}