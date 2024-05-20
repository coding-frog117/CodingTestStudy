package Programmers.lv2;

import java.util.*;

public class 윤찬_Day03_하노이의탑 {

    class Solution {

        List<int[]> list;

        public int[][] solution(int n) {
            int[][] answer;
            list = new ArrayList<>();

            hanoi(n, 1, 2, 3);

            answer = new int[list.size()][2];
            for(int i = 0; i < list.size(); i++) {
                answer[i] = list.get(i);
            }
            return answer;
        }

        public void hanoi(int n, int start, int mid, int end) {

            if(n == 0){
                //System.out.println("return");
                return;
            }

            hanoi(n - 1, start, end, mid);
            list.add(new int[]{start, end});
            //System.out.println("start: " + start + ", end: " + end);
            hanoi(n - 1, mid, start, end);

        }
    }

}
