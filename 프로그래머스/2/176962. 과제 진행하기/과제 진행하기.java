import java.util.*;
import java.util.stream.*;


class Solution {
    
    private int toMin(String time) {
        String[] parsed = time.split(":");
        return Integer.parseInt(parsed[0])*60 + Integer.parseInt(parsed[1]);
    }
    
    class Plan {
        public String name;
        public int start;
        public int playTime;
        
        public Plan(String name, int start, int playTime) {
            this.name = name;
            this.start = start;
            this.playTime = playTime;
        }
        
        @Override
        public String toString() {
            return name + " " + start + " " + playTime;
        }
    }
    
    public String[] solution(String[][] plans) {
        List<String> answer = new ArrayList<>();
        
        Arrays.sort(plans, (a, b) -> Integer.compare(toMin(a[1]), toMin(b[1])));
        
        Deque<Plan> stack = new ArrayDeque<>();
        
        
        int currentTime = 0;
        
        for (String[] plan : plans) {
            Plan newPlan = new Plan(plan[0], toMin(plan[1]), Integer.parseInt(plan[2]));

            while (!stack.isEmpty()) {
                Plan prevPlan = stack.peekLast();
                if (newPlan.start < currentTime + prevPlan.playTime) {
                    Plan p = stack.pollLast();
                    p.playTime -= newPlan.start - currentTime;
                    stack.addLast(p);
                    break;
                }
                stack.pollLast();
                answer.add(prevPlan.name);
                currentTime += prevPlan.playTime;
            }
            currentTime = newPlan.start;
            stack.addLast(newPlan);
        }
        
        while (!stack.isEmpty()) {
            answer.add(stack.pollLast().name); 
        }
        
        return answer.toArray(new String[0]);
    }
}