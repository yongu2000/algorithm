import java.util.*;

class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int answer = 0;
        int left = 1;
        int right = Arrays.stream(diffs).max().getAsInt();
        
        while (left <= right) {
            int mid = (left + right) / 2;
            long time = (long) times[0];
            for (int i = 1; i < diffs.length; i++) {
                if (mid < diffs[i]) {
                    time += (times[i] + times[i-1]) * (diffs[i] - mid) + times[i];
                } else {
                    time += times[i];
                }
            }
            if (time <= limit) {
                right = mid - 1;
                answer = mid;
            } else {
                left = mid + 1;
            }
        }

        return answer;
    }
}