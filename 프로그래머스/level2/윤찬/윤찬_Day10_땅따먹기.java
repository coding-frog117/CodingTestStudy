package Programmers.lv2;

import java.util.Arrays;

public class 윤찬_Day10_땅따먹기 {

    class Solution {
        int solution(int[][] land) {
            int answer = 0;

            int[][] res = new int[land.length][4];

            res[0] = land[0];

            for(int i = 1; i < land.length; i++){
                for(int j = 0; j < 4; j++){
                    int max = 0;
                    for(int k = 0; k < 4; k++){
                        if(j != k){
                            max = Math.max(max, res[i-1][k]);
                        }
                    }
                    res[i][j] = land[i][j] + max;
                }
            }

            for(int v: res[land.length-1]){
                answer = Math.max(answer, v);
            }

            return Arrays.stream(res[land.length - 1]).max().orElse(0);
        }
    }
}
