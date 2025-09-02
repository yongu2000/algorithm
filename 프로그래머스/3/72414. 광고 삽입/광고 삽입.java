import java.util.*;

class Solution {
    
    class Log {
        public int start, end;
        
        public Log(int start, int end) {
            this.start = start;
            this.end = end;
        }
        @Override
        public String toString() {
            return "[" + start + ", " + end + "]";
        }
    }
    
    private int timeToSec(String time) {
        String[] parsed = time.split(":");
        return Integer.parseInt(parsed[0])*60*60 + Integer.parseInt(parsed[1])*60 + Integer.parseInt(parsed[2]);
    }
    
    private String secToTime(int sec) {
        int hour = sec / 3600;
        int min = sec / 60 - hour*60;
        int s = sec % 60;
        return (hour < 10 ? "0" + hour : hour) + ":" 
            + (min < 10 ? "0" + min : min) + ":" 
            + (s < 10 ? "0" + s : s);
    }
    
    public String solution(String play_time, String adv_time, String[] logs) {
		int playTime = timeToSec(play_time);
		int advTime = timeToSec(adv_time);
		
		int[] ad = new int[360_000];
		
		for(String log : logs) {
			String[] l = log.split("-");
			int start = timeToSec(l[0]);
			int end =  timeToSec(l[1]);
			for(int i = start; i < end; i++) {
				ad[i]++;
			}
		}
        
		int maxIdx = 0;
		long maxSum = 0;
		long sum = 0;
		for(int i = 0; i < advTime; i++) {
			sum += ad[i];
		}
		maxSum = sum;
		
		for(int i = advTime; i < playTime; i++) {
			sum += ad[i] - ad[i-advTime];
			if(sum > maxSum) {
				maxSum = sum;
				maxIdx = i-advTime+1;
			}
		}
		
		return secToTime(maxIdx);
    }
}