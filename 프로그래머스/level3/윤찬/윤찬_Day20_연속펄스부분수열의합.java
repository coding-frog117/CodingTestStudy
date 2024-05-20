package Programmers.lv3;

public class 윤찬_Day20_연속펄스부분수열의합 {

    class Solution {
        public long solution(int[] sequence) {
            long answer = 0;

            int[] arr1 = new int[sequence.length];
            int[] arr2 = new int[sequence.length];

            for(int i = 0; i < sequence.length; i++){
                if(i % 2 == 0){
                    arr1[i] = sequence[i];
                    arr2[i] = -sequence[i];
                }else {
                    arr1[i] = -sequence[i];
                    arr2[i] = sequence[i];
                }
            }

            long arr1_sum = maxValue(arr1);
            long arr2_sum = maxValue(arr2);

            answer = Math.max(arr1_sum, arr2_sum);
            return answer;
        }

        long maxValue(int[] A){
            long maxSum, sum;
            int k;
            maxSum = 0;
            sum = 0;
            for (k = 0; k < A.length; k++) {
                sum = (long)Math.max(sum + A[k], 0);
                maxSum = (long)Math.max(maxSum, sum);
            }
            return maxSum;
        }
    }
}
