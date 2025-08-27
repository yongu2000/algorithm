import java.util.*;

class Solution {
    
    
    private void dfs(int n, int[] info, int last, int[] temp) {
        
        for (int i = last; i < 11; i++) {
            if (n > info[i]) {                
                int[] temp2 = Arrays.copyOf(temp, temp.length);
                temp2[i] = info[i] + 1;
                if (info[i] > 0) {
                    temp2[11] -= (10-i);                
                }
                temp2[12] += (10-i);
                temp2[13] = n-info[i]-1;
                
                dfs(n-info[i]-1, info, i+1, temp2);
            }
            dfs(n, info, i+1, temp);
            
        }
        ansList.add(Arrays.copyOf(temp, temp.length));
        
    }
    
    List<int[]> ansList;
    
    public int[] solution(int n, int[] info) {
        ansList = new ArrayList<>();
        
        int[] temp = new int[14];
        for (int i = 0; i < info.length; i++) {
            if (info[i] != 0) {
                temp[11] += 10-i;               
            }
        }
        temp[13] = n;
        
        dfs(n, info, 0, temp);
        
        Collections.sort(ansList, (a, b) -> {
            if (b[12] - b[11] == a[12] - a[11]) {
                for (int i = 0; i < 10; i++) {
                    if (b[10-i] == a[10-i]) continue;
                    return Integer.compare(b[10-i], a[10-i]);
                }
            }
            return Integer.compare(b[12] - b[11], a[12] - a[11]);  
            });
        
        int[] ans = ansList.get(0);
        if (ans[12] <= ans[11]) {
            return new int[]{-1};
        } else {
            ans[10] += ans[13];
        }
        return Arrays.copyOfRange(ans, 0, 11);

    }
}