import java.util.*;
import java.util.stream.*;

class Solution {
    
    private void permutation(int[] arr, int depth, List<int[]> result) {
    
        if (arr.length == depth) {
            result.add(arr.clone());
            return;
        }
        
        for (int i = depth; i < arr.length; i++) {
            swap(arr, depth, i);
            permutation(arr, depth + 1, result);
            swap(arr, depth, i);
        }
    }
    
    private void swap(int[] arr, int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
    
    public int solution(int n, int[] weak, int[] dist) {
        int answer = 10;
        int len = weak.length;

        // weak 배열 확장 (원형 -> 직선)
        int[] extended = new int[len * 2];
        for (int i = 0; i < len * 2; i++) {
            if (i < len) extended[i] = weak[i];
            else extended[i] = weak[i - len] + n;
        }
        
        List<int[]> permutations = new ArrayList<>();
        permutation(dist, 0, permutations);

        for (int start = 0; start < len; start++) {
            for (int[] friends : permutations) {
                int cnt = 1;
                int position = extended[start] + friends[cnt-1];
                
                for (int idx = start; idx < start + len; idx++) {
                    if (extended[idx] > position) {
                        cnt++;
                        if (cnt > friends.length) break;
                        position = extended[idx] + friends[cnt-1];
                    }
                }
                answer = Math.min(answer, cnt);
                
            }
        }
        
        return (answer > dist.length) ? -1 : answer;
    }
}