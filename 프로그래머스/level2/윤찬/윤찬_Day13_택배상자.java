package Programmers.lv2;

import java.util.*;

public class 윤찬_Day13_택배상자 {

    class Solution {
        public int solution(int[] order) {
            int answer = 0;

            Stack<Integer> stk = new Stack<>();
            int start = 1;
            for(int o: order) {

                if(start < o) {
                    while(start < o){
                        stk.add(start);
                        start++;
                    }
                }

                if(o == start) {
                    answer++;
                    start++;
                }else {
                    if(stk.isEmpty()){
                        break;
                    }else {
                        if(stk.peek() != o) {
                            break;
                        }else {
                            answer++;
                            stk.pop();
                        }
                    }
                }

            }

            return answer;
        }
    }
}
