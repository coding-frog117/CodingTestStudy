package baekjoon;

import java.util.*;

public class pb1021 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int nums = sc.nextInt();

        int[] values = new int[nums];
        for(int i = 0; i < nums; i++) {
            values[i] = sc.nextInt();
        }

        Deque<Integer> deque = new ArrayDeque<>();
        for(int i = 1;  i <= n; i++) {
            deque.add(i);
        }

        int answer = 0;

        for(int i : values) {
            int pos = List.copyOf(deque).indexOf(i);
            if(pos == 0) {
                deque.poll();
            }else {
                int min = Math.min(Math.abs(pos), Math.abs(deque.size() - pos));
                answer += min;
                if(min == pos) {
                    for(int j = 0; j < min; j++ ){
                        if(!deque.isEmpty()){
                            int v = deque.poll();
                            deque.add(v);
                        }
                    }
                }else {
                    for(int j = 0; j < min; j++ ){
                        if(!deque.isEmpty()){
                            int v = deque.pollLast();
                            deque.addFirst(v);
                        }
                    }
                }
                deque.poll();
            }

        }

        System.out.println(answer);
    }
}
