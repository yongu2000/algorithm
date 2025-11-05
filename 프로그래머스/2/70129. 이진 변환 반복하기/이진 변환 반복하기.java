import java.util.*;

class Solution {
    public int[] solution(String s) {      
        int times = 0;
        int zeros = 0;
        
        while (s.length() != 1) {
            int zero = 0;
            
            for (char c : s.toCharArray()) {
                if (c == '0') zero++;
            }
            int ones = s.length() - zero;
            
            zeros += zero;
            times++;
            
            s = Integer.toBinaryString(ones);
        }
        
        return new int[]{times, zeros};
    }
}