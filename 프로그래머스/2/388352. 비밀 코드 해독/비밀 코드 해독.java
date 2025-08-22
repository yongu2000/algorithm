import java.util.*;
import java.util.stream.*;


class Solution {
    
    
    private void makeCombinations(int[] nums, int c, List<Integer> temp) {
        if (temp.size() == c) {
            combinations.add(new HashSet<>(temp));
            return;
        }
        
        for (int i = 1; i <= nums.length; i++) {
            if (temp.isEmpty() || temp.get(temp.size()-1) < i) {
                temp.add(i);
                makeCombinations(nums, c, temp);
                temp.remove(temp.size()-1);
            }
        }
        
    }
    
    private List<Set<Integer>> combinations;
    
    public int solution(int n, int[][] q, int[] ans) {
        int answer = 0;
        combinations = new ArrayList<>();
        int[] nums = new int[n];
        for (int i = 1; i <= n; i++) {
            nums[i-1] = i;
        }
        
        makeCombinations(nums, 5, new ArrayList<>());
        
        for (Set<Integer> combination : combinations) {
            int hits = 0;
            for (int i = 0; i < q.length; i++) {
                Set<Integer> qSet = Arrays.stream(q[i]).boxed().collect(Collectors.toSet());
                qSet.retainAll(combination);
                if (qSet.size() == ans[i]) {
                    hits++;
                }
            }
            
            if (hits == ans.length) {
                answer++;
            }
        }
  
        return answer;
    }
}