package Programmers.lv2;

public class 윤찬_Day04_연속된부분수열의합 {

    class Solution {
        public int[] solution(int[] sequence, int k) {
            int[] answer = {};


            int start = 0;
            int end = 0;
            int len = Integer.MAX_VALUE;
            int value = 0;
            while(start != sequence.length) {

                if(value >= k) {
                    if(value == k && len > end - start){
                        answer = new int[]{start, end - 1};
                        len = end - start;
                    }
                    value -= sequence[start++];
                } else {
                    //값이 작은 경우
                    if(end == sequence.length) break;
                    value += sequence[end++];
                }

            }


            return answer;
        }
    }
}
