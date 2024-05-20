package Programmers.lv2;

public class 윤찬_Day11_2n타일 {

    class Solution {
        public int solution(int n) {
            int answer = 0;

            long[] res = new long[n + 1];

            res[1] = 1;
            res[2] = 2;

            for (int i = 3; i <= n; i++) {
                res[i] = (res[i - 1] + res[i - 2]) % 1_000_000_007;
            }

            return  (int)res[n];
        }
    }
}
