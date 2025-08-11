import java.util.*;
import java.io.*;

public class Main {
    public static void main(String args[]) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(reader.readLine());

        for (int i = 0; i < n; i++) {
            String arr = reader.readLine();
            int score = 0;
            int o = 0;
            for (char a : arr.toCharArray()) {
                if (a == 'O') {
                    o++;
                } else {
                    o = 0;
                }
                score += o;
            }
            writer.append(Integer.toString(score));
            writer.append("\n");
        }

        writer.flush();
    }
}