package baekjoon;

import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;

public class pb17298 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        //Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[n];
        int[] res = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Stack<Integer> stk = new Stack<>();

        for (int i = 0; i < n; i++) {
            while (!stk.isEmpty() && arr[stk.peek()] < arr[i]) {
                int pop_index = stk.pop();
                res[pop_index] = arr[i];
            }
            stk.push(i);

        }

        while (!stk.isEmpty()) {
            res[stk.pop()] = -1;
        }

        for(int i : res){
            bw.write(i + " ");
        }
        bw.write("\n");

        bw.flush();
        bw.close();
        br.close();
    }
}
