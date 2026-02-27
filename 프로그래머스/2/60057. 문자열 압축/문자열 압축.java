import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = s.length();
        
        StringBuilder sb = new StringBuilder(s);
        
        for (int i = 1; s.length() / i >= 2; i++) {
            int start = 0;
            int end = (start+1)*i;
            
            // System.out.println(i + ": ==============");
            String prev = "";
            int length = 0;
            int tempLength = 0;
            while (end <= s.length()) {
                // System.out.println("-------");
                
                String current = sb.substring(start, end);
//                 System.out.println("current : " + current);
//                 System.out.println("prev : " + prev);
                
//                 System.out.println("prev LENGTH: " + length);
//                 System.out.println("prev TEMP LENGTH: " + tempLength);
                if (prev.equals(current)) {
                    // System.out.println("equals");
                    if (tempLength == 0) tempLength++;
                    tempLength++;
                } else {
                    // System.out.println("different");
                    if (!prev.isEmpty() && tempLength != 0) length += String.valueOf(tempLength).length();
                    length += i;
                    // System.out.println("different :" + length);
                    
                    prev = current;
                    tempLength = 0;
                }
                // System.out.println("LENGTH: " + length);
                // System.out.println("TEMP LENGTH: " + tempLength);
                
                start+=i;
                end+=i;
            }
            if (tempLength != 0) length += String.valueOf(tempLength).length();
            answer = Math.min(answer, length + (s.length() % i));
            // System.out.println(answer);
            
        }
        return answer;
    }
}