import java.util.*;

class Solution {
    
    private boolean isBalanced(String p) {
        int count = 0;
        for (char c : p.toCharArray()) {
            if (c == '(') count++;
            else count--;
        }
        return count == 0;
    }
    
    private boolean isCorrect(String p) {
        int count = 0;
        for (char c : p.toCharArray()) {
            if (c == '(') count++;
            else {
                if (count == 0) return false; 
                count--;
            }
        }
        return count == 0;
    }
    
    private String[] separateString(String p) {
        String[] result = new String[2];
        StringBuilder sb = new StringBuilder();
        
        boolean separated = false;
        for (char c : p.toCharArray()) {
            sb.append(c);
            if (isBalanced(sb.toString()) && !separated) {
                result[0] = sb.toString();
                separated = true;
                sb.setLength(0);
            }
        }
        result[1] = sb.toString();
        return result;
    }
    
    private String solve(String p) {
        if (p.isEmpty()) return "";
        if (isCorrect(p)) return p;
        
        String[] separate = separateString(p);
        String u = separate[0];
        String v = separate[1];

        if (isCorrect(u)) return u + solve(v);
        
        StringBuilder sb = new StringBuilder();
        sb.append("(");
        sb.append(solve(v));
        sb.append(")");
        
        for (char c : u.substring(1, u.length() -1).toCharArray()) {
            if (c == '(') sb.append(')');
            else sb.append('(');
        }
        return sb.toString();      
    }
    
    public String solution(String p) {
        return solve(p);
    }
}