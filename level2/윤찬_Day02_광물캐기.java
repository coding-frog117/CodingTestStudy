package Programmers.lv2;

import java.util.*;

public class 윤찬_Day02_광물캐기 {


    class Solution {
        String[] m;
        int answer;

        public int solution(int[] picks, String[] minerals) {
            answer = Integer.MAX_VALUE;
            m = minerals;

            dfs(picks, 0, 0);

            return answer;
        }

        public void dfs(int[] picks, int index ,int point ) {

            if(Arrays.stream(picks).sum() == 0 || 5*index  >= m.length){
                answer = Math.min(answer, point);
                return;
            }

            for(int i = 0; i < picks.length; i++){
                if(picks[i] > 0) {
                    int new_point = getPoint(index, i);
                    int[] new_pick = picks.clone();
                    new_pick[i]--;
                    dfs(new_pick, index + 1, point + new_point);
                }
            }
        }

        public int getPoint(int index, int type){
            int len = 5 * index + 5 >= m.length ? m.length : 5*index + 5;
            // if(5 * index + 5 >= m.length)
            //     len = m.length;
            // else
            //     len = 5*index + 5;
            int sum = 0;
            for(int i = 5 * index; i < len; i++){
                switch(m[i]){
                    case "diamond":
                        if(type == 2){
                            sum += 25;
                        }else if(type == 1){
                            sum += 5;
                        }else {
                            sum += 1;
                        }
                        break;
                    case "iron":
                        if(type == 2) {
                            sum += 5;
                        }else {
                            sum += 1;
                        }
                        break;
                    case "stone":
                        sum += 1;
                        break;
                }
            }
            return sum;
        }
    }
}
