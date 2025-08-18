class Solution {
    public long solution(int w, int h) {
        long answer = 0;
        long idx = 0;

        for (long i = 1; i <= w; i++) {
            idx = i;
            long ceil = (h * i + w - 1) / w;
            long floor = (h * (i - 1)) / w;
            answer += ceil - floor;

            if ((h * i) % w == 0) {
                break;
            }
        }

        answer *= (w / idx);
        return (long) w * (long) h - answer;
    }
}