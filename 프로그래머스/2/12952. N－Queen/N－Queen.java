import java.util.*;

class Solution {
    
    private void nQueen(int n, List<Integer> temp) {
        if (temp.size() == n) {
            answer++;
            return;
        }
        
        int i = temp.size();
        Set<Integer> possible = new HashSet<>();
        for (int idx = 0; idx < n; idx++) {
            possible.add(idx);
        } 

        for (int j = 0; j < temp.size(); j++) {
            possible.remove(temp.get(j));                
            if (temp.get(j) - (i - j) >= 0) possible.remove(temp.get(j) - (i - j));
            if (temp.get(j) + (i - j) < n) possible.remove(temp.get(j) + (i - j));     
        }

        for (Integer p : possible) {
            temp.add(p);
            nQueen(n, temp);
            temp.remove(temp.size()-1);
        }
    }
    
    private int answer;
    
    public int solution(int n) {
        answer = 0;
        nQueen(n, new ArrayList<>());
        return answer;
    }
}