import java.util.*;
class Solution {
    
    private Set<String> opSet;
    
    private String[] operands = {"+", "-", "*"};
    private boolean[] visited = {false, false, false};
    
    private void makeOperandSet(String t) {
        if (t.length() == 3) {
            opSet.add(t);
            return;
        }
        
        for (int i = 0; i < 3; i++) {
            if (!visited[i]) {
                visited[i] = true;
                makeOperandSet(t + operands[i]);
                visited[i] = false;
            }  
        } 
    }
    
    	
    private String calc(String num1, String op, String num2) {
        long n1 = Long.parseLong(num1);
        long n2 = Long.parseLong(num2);
 
        if (op.equals("+"))
            return n1 + n2 + "";
        else if (op.equals("-"))
            return n1 - n2 + "";
        return n1 * n2 + "";
    }
    
    public long solution(String expression) {
        long answer = 0;
        
        opSet = new HashSet<>();
        String[] split = expression.split("(?<=[-+*/])|(?=[-+*/])");
        
        makeOperandSet("");
        
        long max = Long.MIN_VALUE;
        long min = Long.MAX_VALUE;
        
        for (String op : opSet) {
            List<String> list = new ArrayList<>(List.of(split));
            for (char o : op.toCharArray()) {
                for (int i = 0; i < list.size(); i++) {
                    if (list.get(i).equals(String.valueOf(o))) {
                        list.set(i-1, calc(list.get(i-1), list.get(i), list.get(i+1)));
                        list.remove(i);
                        list.remove(i);
                        i--;
                    }   
                }
            }
            answer = Math.max(answer, Math.abs(Long.parseLong(list.get(0))));
        }
        
        return answer;
    }
}