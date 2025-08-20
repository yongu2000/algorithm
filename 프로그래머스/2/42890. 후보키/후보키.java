import java.util.*;

class Solution {
    
    private void candidateKey(Set<Integer> temp, int start) {
        for (int i = start; i < col; i++) {
            if (!visited[i]) {
                visited[i] = true;    
                temp.add(i);
                allKeys.add(new HashSet<>(temp));
                candidateKey(temp, i);
                temp.remove(i);
                visited[i] = false;    
            }
        }
    }
    
    private List<Set<Integer>> allKeys;
    private boolean[] visited;
    private int col;
    private int row;
    
    public int solution(String[][] relation) {
        allKeys = new ArrayList<>();
        
        row = relation.length;
        col = relation[0].length;
        
        visited = new boolean[col];
        
        candidateKey(new HashSet<>(), 0);
        
        System.out.println(allKeys);
        
        // 유일성 검사
        List<Set<Integer>> possibleKeys = new ArrayList<>();
        
        for (Set<Integer> keys : allKeys) {
            Set<List<String>> duplicates = new HashSet<>();
            
            for (int i = 0; i < relation.length; i++) {
                List<String> temp = new ArrayList<>();
                for (int key : keys) {
                    temp.add(relation[i][key]);
                }
                duplicates.add(temp);
            }
            System.out.println(keys);
            
            System.out.println(duplicates);
            
            if (duplicates.size() == relation.length) {
                possibleKeys.add(keys);
            }
        }
        
        
        // 최소성 검사

        Collections.sort(possibleKeys, (a, b) -> Integer.compare(a.size(), b.size()));
        
        System.out.println(possibleKeys);
        
        int idx = -1;
        int size = 0;
        
        List<Set<Integer>> candidateKeys = new ArrayList<>();
        for (Set<Integer> key : possibleKeys) {
            boolean flag = true;
            for (Set<Integer> candKey : candidateKeys) {
                if (key.containsAll(candKey)) {
                    System.out.println(key + "는 " + candKey + "를 포함합니다.");
                    
                    flag = false;
                    break;
                }
            }
            if (flag) {
                candidateKeys.add(key);
            }
        }
        
        System.out.println(candidateKeys);
        
        
        return candidateKeys.size();
    }
}