import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String s) {
        List<Integer> intArr = Arrays.stream(s.split(" ")).mapToInt(Integer::parseInt).boxed().collect(Collectors.toList());      
        return Collections.min(intArr) + " " + Collections.max(intArr);
    }
}