import java.util.*;

class Solution {
  
    private int lowerBound(List<Integer> list, int target) {
        int left = 0;
        int right = list.size()-1;
        
        while (left <= right) {
            int mid = (left + right) / 2;
            if (target <= list.get(mid)) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return list.size() - left;
    }
    
    public int[] solution(String[] info, String[] query) {        
        Map<String, List<Integer>> index = new HashMap<>();
        
        for (String language : new String[]{"-", "cpp", "java", "python"}) {
            for (String position : new String[]{"-", "backend", "frontend"}) {
                for (String year : new String[]{"-", "junior", "senior"}) {
                    for (String food : new String[]{"-", "chicken", "pizza"}) {
                        index.put(language + position + year + food, new ArrayList<>());
                    }
                }
            }
        }
        
        for (String i : info) {
            String[] split = i.split(" ");
            for (String language : new String[]{"-", split[0]}) {
                for (String position : new String[]{"-", split[1]}) {
                    for (String year : new String[]{"-", split[2]}) {
                        for (String food : new String[]{"-", split[3]}) {
                            index.get(language + position + year + food).add(Integer.parseInt(split[4]));
                        }
                    }
                }
            }
        }
        
        for (List<Integer> val : index.values()) {
            Collections.sort(val);
        }
        // System.out.println(index);
        
        int[] answer = new int[query.length];
        
        for (int i = 0; i < query.length; i++) {
            String[] split = query[i].replace(" and ", " ").split(" ");
            answer[i] = lowerBound(index.get(split[0] + split[1] + split[2] + split[3]), Integer.parseInt(split[4]));
        }
        
        return answer;
    }
}