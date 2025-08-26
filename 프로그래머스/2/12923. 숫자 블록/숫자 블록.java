import java.util.*;

class Solution {
    public int[] solution(long begin, long end) {
        int size = (int) (end - begin);
        int[] answer = new int[size + 1];
        
        for (int i = 0; i <= size; i++) {
            long index = begin + i;
            
            for (long div = 2; div <= Math.sqrt(index); div++) {
                if (index % div == 0) {
                    if (index / div > 10000000) {
                        answer[i] = (int) div;
                        continue;
                    } else {
                        answer[i] = (int) (index / div);
                    }
                    break;
                }
            }
            if (answer[i] == 0) answer[i] = 1;
        }
        if (begin == 1) answer[0] = 0;
        return answer;
    }
}