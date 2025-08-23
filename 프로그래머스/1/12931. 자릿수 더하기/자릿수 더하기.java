import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        
        String num = String.valueOf(n);
        
        for (char c : num.toCharArray()) {
            answer += Integer.parseInt(String.valueOf(c));
        }

        System.out.println("Hello Java");

        return answer;
    }
}