package Programmers.lv2;

import java.util.*;

public class 윤찬_Day08_다리를지나는트럭 {

    class Solution {
        public int solution(int bridge_length, int weight, int[] truck_weights) {
            int answer = 0;

            Queue<W> queue = new LinkedList<>();
            Queue<Integer> delay = new LinkedList<>();

            for(int d: truck_weights){
                delay.add(d);
            }
            int time = 0;

            while(!delay.isEmpty() || !queue.isEmpty()) {
                //System.out.print("time : " + time + ", ");
                if(!queue.isEmpty()){
                    if(time - queue.peek().time >= bridge_length) {
                        //System.out.print("out: " + queue.peek().weight +", ");
                        queue.poll();
                    }
                }

                int sum = queue.isEmpty() ? 0 : queue.stream().mapToInt(w -> w.weight).sum();

                if(!delay.isEmpty()) {
                    if(sum + delay.peek() <= weight){
                        //System.out.print("add : " + delay.peek() + ", ");
                        queue.add(new W(delay.poll(), time));
                    }
                }
                //System.out.println();
                time++;
            }

            answer = time;
            return answer;
        }

        public class W {
            int weight;
            int time;

            public W(int weight, int time) {
                this.weight = weight;
                this.time = time;
            }
        }

    }
}
