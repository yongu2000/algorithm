import java.util.*;

class Solution {
    public String[] solution(String[] s) {
        List<String> answer = new ArrayList<>();
        
        for (String str : s) {
            Deque<Character> stack = new ArrayDeque<>();
            int cnt = 0;
            
            for (char c : str.toCharArray()) {
                stack.add(c);
                
                if (stack.size() >= 3) {
                    char c3 = stack.pollLast();
                    char c2 = stack.pollLast();
                    char c1 = stack.pollLast();
                    
                    if (c1 == '1' && c2 == '1' && c3 == '0') cnt++;
                    else {
                        stack.add(c1);
                        stack.add(c2);
                        stack.add(c3);
                    }
                }
            }
            
            StringBuilder sb = new StringBuilder();
            for (char c : stack) sb.append(c);
            String temp = sb.toString();
            
            int idx = temp.lastIndexOf('0');
            String insert = "110".repeat(cnt);
            
            if (idx == -1) {
                temp = insert + temp;
            } else {
                temp = temp.substring(0, idx + 1) + insert + temp.substring(idx + 1);
            }
            answer.add(temp);
        }
        return answer.toArray(new String[0]);
    }
}