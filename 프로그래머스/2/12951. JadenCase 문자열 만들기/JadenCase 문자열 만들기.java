import java.util.*;

class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        
        boolean jaden = true;
        
        for (char c : s.toCharArray()) {
            if (Character.isAlphabetic(c) && jaden) {
                sb.append(Character.toUpperCase(c));
            } else {
                sb.append(Character.toLowerCase(c));
            }
            jaden = false;
            
            if (c == ' ') jaden = true;
        }

        return sb.toString();
    }
}