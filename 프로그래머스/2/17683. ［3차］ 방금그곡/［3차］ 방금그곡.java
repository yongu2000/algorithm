import java.util.*;

class Solution {
    
    
    class MusicInfo {
        
        private int start;
        private int end;
        private String name;
        private List<String> music = new ArrayList<>();
        
        public MusicInfo(String[] musicInfo) {
            this.start = timeToMin(musicInfo[0]);
            this.end = timeToMin(musicInfo[1]);
            this.name = musicInfo[2];
            
            int idx = 0;
            for (char c : musicInfo[3].toCharArray()) {
                if (c == '#') {
                    music.set(idx-1, String.valueOf(music.get(idx-1) + c));
                } else {
                    music.add(idx, String.valueOf(c));
                    idx++;
                } 
            }
        }
        
        public int getStart() {
            return this.start;
        } 
        public int getEnd() {
            return this.end;
        }
        public String getName() {
            return this.name;
        }
        public List<String> getMusic() {
            return this.music;
        }
        
        public List<String> getFullMusic() {
            int time = end - start;
            
            if (music.size() > time) {
                return music.subList(0, time);
            }
            
            List<String> fullMusic = new ArrayList<>(music);
            for (int i = 0; i < time / music.size(); i++) {
                fullMusic.addAll(music);
            }
            
            return fullMusic.subList(0, time);
        }
        
        private int timeToMin(String time) {
            String[] parse = time.split(":");
            int hour = Integer.parseInt(parse[0]);
            int min = Integer.parseInt(parse[1]);

            return hour*60 + min;
        }
        
        @Override
        public String toString() {
            return start + " "  + end + " " + name + " " + music.toString();
        }
    }
    
    private List<String> getMelodyList(String m) {
        List<String> melody = new ArrayList<>();
        int idx = 0;
        for (char c : m.toCharArray()) {
            if (c == '#') {
                melody.set(idx-1, String.valueOf(melody.get(idx-1) + c));
            } else {
                melody.add(idx, String.valueOf(c));
                idx++;
            } 
        }
        return melody;
    }
    
    public String solution(String m, String[] musicinfos) {
        String answer = "(None)";
        int ansLen = 0;
        for (String musicinfo : musicinfos) {
            MusicInfo info = new MusicInfo(musicinfo.split(","));
            List<String> melody = getMelodyList(m);
            List<String> fullMusic = info.getFullMusic();

            boolean same = false;
            for (int i = 0; i < fullMusic.size() - melody.size() + 1; i++) {
                // System.out.println("============");
                same = true;
                for (int j = 0; j < melody.size(); j++) {
                    // System.out.println(fullMusic.get(i+j) + " " + melody.get(j));
                    if (!fullMusic.get(i+j).equals(melody.get(j))) {
                        same = false;
                        break;
                    }
                }
                if (same) {
                    break;
                }
            }
            
            if (same) {
                if (fullMusic.size() > ansLen) {
                    ansLen = fullMusic.size();
                    answer = info.getName();
                }
            }
            
            
            // System.out.println(info);
            // System.out.println(info.getFullMusic());
            // System.out.println(melody.toString());
        }
        return answer;
    }
}