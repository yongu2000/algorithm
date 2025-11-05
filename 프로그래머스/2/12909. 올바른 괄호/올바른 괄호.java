import java.util.*;

class Solution {
    boolean solution(String s) {
        Deque<Character> deque = new ArrayDeque<>();
        
        for (char c : s.toCharArray()) {
            if (c == ')' && !deque.isEmpty() && deque.peekLast() == '(') {
                deque.pollLast();                
            } else {
                deque.addLast(c);
            }
        }

        return deque.isEmpty();
    }
}