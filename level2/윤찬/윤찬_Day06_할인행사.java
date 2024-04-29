package Programmers.lv2;

import java.util.HashMap;
import java.util.Map;

public class 윤찬_Day06_할인행사 {

    class Solution {
        Map<String, Integer> map = new HashMap<>();

        public int solution(String[] want, int[] number, String[] discount) {
            int answer = 0;


            for(int i = 0; i < 10; i++){
                map.put(discount[i], map.getOrDefault(discount[i], 0) + 1);
            }

            if(check(want, number)) answer++;

            for(int i = 10; i < discount.length; i ++) {
                map.put(discount[i - 10], map.getOrDefault(discount[i - 10], 0) - 1 );
                map.put(discount[i], map.getOrDefault(discount[i], 0) + 1);

                if(check(want, number)){
                    answer++;
                }

            }

            return answer;
        }

        public boolean check(String[] want, int[] number){
            for(int i = 0; i < want.length; i++) {
                if(map.getOrDefault(want[i], 0) != number[i]) return false;
            }
            return true;
        }
    }
}
