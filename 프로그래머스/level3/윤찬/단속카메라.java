package Programmers.lv3;

import java.util.Arrays;

public class 단속카메라 {

    class Solution {
        public int solution(int[][] routes) {
            int answer = 1;

            Arrays.sort(routes, (o1, o2) -> {
                if(o1[1] == o2[1]) return o1[0] - o2[0];
                else return o1[1] - o2[1];
            });

            int end = routes[0][1];
            for(int i = 1; i <routes.length; i++){
                if(end < routes[i][0]){
                    end = routes[i][1];
                    answer++;
                }
            }

            return answer;
        }
    }
}
