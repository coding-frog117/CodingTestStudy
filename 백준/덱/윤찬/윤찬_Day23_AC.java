package baekjoon;

import java.io.*;
import java.util.*;

public class pb5430 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//        Scanner sc = new Scanner(System.in);
        //테스트 케이스
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            //패턴
            String p = br.readLine();

            //배열의 수
            int n = Integer.parseInt(br.readLine());

            //배열 정의
            String a = br.readLine();
            if(a.equals("[]")) {
                if(n != 0){
                    bw.write("error\n");
//                System.out.println("error");
                    continue;
                }
            }
            String[] values = a.substring(1, a.length() - 1).split(",");
            //System.out.println("values" + values.length);
            //int[] arr = new int[n];
            Deque<Integer> deque = new ArrayDeque<>();
            for (String value : values) {
                if(!value.isEmpty()) {
                    deque.add(Integer.parseInt(value));
                }
            }

            boolean reverse = false;
            boolean error = false;

            for (String s : p.split("")) {
                if (s.equals("R")) {
                    reverse = !reverse;
                } else {
                    if (deque.isEmpty()) {
                        error = true;
                        break;
                    } else {
                        if (reverse)
                            deque.pollLast();
                        else
                            deque.pollFirst();
                    }
                }
            }

            if(error) {
                bw.write("error\n");
//                System.out.println("error");
            }else {
                List<Integer> l = new ArrayList<>();
                if(reverse){
                    while (!deque.isEmpty()){
                        l.add(deque.pollLast());
                    }
                }else {
                    while (!deque.isEmpty()){
                        l.add(deque.pollFirst());
                    }
                }

                bw.write("[");
//                System.out.print("[");
                for(int j = 0; j < l.size(); j++){
                    bw.write(String.valueOf(l.get(j)));
//                    System.out.print(l.get(j));
                    if(j != l.size()-1){
                        bw.write(",");
//                        System.out.print(",");
                    }
                }
                bw.write("]\n");
//                System.out.println("]");
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
