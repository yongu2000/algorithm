import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(long n) {
        String[] str = new StringBuilder(String.valueOf(n)).reverse().toString().split("");
        
        return Arrays.stream(str).map(Integer::parseInt).mapToInt(Integer::intValue).toArray();
    }
}