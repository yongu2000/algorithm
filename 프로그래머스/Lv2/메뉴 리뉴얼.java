// https://school.programmers.co.kr/learn/courses/30/lessons/118667

import java.util.*;
import java.util.stream.*;

class Solution {
                                        
    static void dfs(char[] options, Map<String, Integer> map, String s, int n) {
        if (s.length() == n) {
            map.put(s, map.getOrDefault(s, 0)+1);
            return;
        }  
        for (char option : options) {
            if (s.isEmpty() || option > s.charAt(s.length()-1)) {
                dfs(options, map, s+option, n);
            }
        }
        return;
    }
   
    public String[] solution(String[] orders, int[] course) {
        List<String> answer = new ArrayList<>();
        
        for (int c : course) {
            Map<String, Integer> map = new HashMap<>();
            int max = -1;
            
            for (String order : orders) {
                dfs(order.toCharArray(), map, "", c);
            }
            for (String key : map.keySet()) {
                max = Math.max(map.get(key), max);
            }
            for (String key : map.keySet()) {
                if (map.get(key) == max && max >= 2) {
                    answer.add(key);
                }
            }
        }
        Collections.sort(answer);
        return answer.toArray(new String[0]);
    }
}

