package Programmers.lv3;

import java.util.*;

public class 윤찬_Day04_숫자게임 {


    class Solution {
        public int solution(int[] A, int[] B) {
            int answer = 0;

            Arrays.sort(A);
            Arrays.sort(B);

            int index = B.length - 1;

            for(int i = A.length - 1; i >= 0; i--){
                if(A[i] < B[index]){
                    answer += 1;
                    index--;
                }
            }

            return answer;
        }
    }
}
