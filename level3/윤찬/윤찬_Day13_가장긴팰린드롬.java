package Programmers.lv3;

public class 윤찬_Day13_가장긴팰린드롬 {

    class Solution
    {
        public int solution(String s)
        {
            int answer = 0;

            if(s.isEmpty()){
                return 0;
            }

            if(s.length() == 1) return 1;

            char[] arr = s.toCharArray();

            for(int i = 0; i < arr.length; i++){
                answer = Math.max(answer, count(arr, i, 1));

                if(i-1 >= 0) {
                    if(arr[i-1] == arr[i]) {
                        answer = Math.max(answer, countEven(arr,i,1, true));
                    }
                }

                if(i+1 < arr.length) {
                    if(arr[i+1] == arr[i]){
                        answer = Math.max(answer, countEven(arr,i,1, false));
                    }
                }
            }

            return answer;
        }

        public int count(char[] arr, int stand, int width) {
            if(stand - width < 0 || stand + width >= arr.length) {
                return 2 * (width - 1) + 1;
            }else {
                if(arr[stand-width] != arr[stand+width]) {
                    return 2 * (width -1) + 1;
                }else {
                    return count(arr,stand, width + 1);
                }
            }
        }

        public int countEven(char[] arr, int stand, int width, boolean isLeft) {

            int left;
            int right;

            if(isLeft) {
                left = stand-width -1;
                right = stand + width;
            }else {
                left = stand-width;
                right = stand + width + 1;
            }

            if(left < 0 || right >= arr.length) {
                return 2 * (width - 1) + 2;
            }else {
                if(arr[left] != arr[right]) {
                    return 2 * (width -1) + 2;
                }else {
                    return countEven(arr,stand, width + 1, isLeft);
                }
            }
        }

    }
}
