import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> answer = new ArrayList<>();
        
        int prev = -1;
        for (int num : arr) {

            if (answer.isEmpty()) {
                prev = num;
                answer.add(num);
                continue;
            } 
            if (prev != num) {
                prev = num;
                answer.add(num);
            }
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}