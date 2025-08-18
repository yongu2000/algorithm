import java.util.*;
import java.util.stream.*;

class Solution {

    public int solution(int[] picks, String[] minerals) {
        int answer = 0;

        int pickCount = Arrays.stream(picks).sum()*5;
        
        String[] left;
        if (minerals.length > pickCount) {
            left = Arrays.copyOfRange(minerals, 0, pickCount);
        } else {
            left = minerals;
        }
        
        List<List<String>> ores = new ArrayList<>();
        
        int idx = 0;
        int cnt = 0;
        for (String ore : left) {
            if (cnt == 0) {
                ores.add(new ArrayList<>());
            }
            ores.get(idx).add(ore);
            cnt++;
            
            if (cnt == 5) {
                cnt = 0;
                idx++;
            }
        }
        
        Collections.sort(ores, (b, a) -> {
            if (Collections.frequency(a, "diamond") == Collections.frequency(b, "diamond")) {
                if (Collections.frequency(a, "iron") == Collections.frequency(b, "iron")) {
                    return Integer.compare(Collections.frequency(a, "stone"), Collections.frequency(b, "stone"));
                }
                return Integer.compare(Collections.frequency(a, "iron"), Collections.frequency(b, "iron"));
            }
            return Integer.compare(Collections.frequency(a, "diamond"), Collections.frequency(b, "diamond"));    
            });

        System.out.println(ores.toString());
        
        for (List<String> ore : ores) {
            if (picks[0] > 0) {
                for (String o : ore) {
                    if (o.equals("diamond")) {
                        answer += 1;
                    } else if (o.equals("iron")) {
                        answer += 1;
                    } else {
                        answer += 1;
                    }
                }
                picks[0]--;
            } else if (picks[1] > 0) {
                for (String o : ore) {
                    if (o.equals("diamond")) {
                        answer += 5;
                    } else if (o.equals("iron")) {
                        answer += 1;
                    } else {
                        answer += 1;
                    }
                }
                picks[1]--;
            } else if (picks[2] > 0) {
                  for (String o : ore) {
                    if (o.equals("diamond")) {
                        answer += 25;
                    } else if (o.equals("iron")) {
                        answer += 5;
                    } else {
                        answer += 1;
                    }
                }  
                picks[2]--;
            } else {
                break;
            }
        }
        return answer;
    }
}