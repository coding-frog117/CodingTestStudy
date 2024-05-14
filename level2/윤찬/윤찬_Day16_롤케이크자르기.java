package Programmers.lv2;

import java.util.HashSet;
import java.util.Set;

public class 윤찬_Day16_롤케이크자르기 {
    class Solution {
        public int solution(int[] topping) {
            int answer = 0;

            int[] count = new int[10001];
            Set<Integer> right = new HashSet<>();
            Set<Integer> left = new HashSet<>();
            for (int j : topping) {
                count[j]++;
                left.add(j);
            }

            for(int i = 0; i < topping.length; i++){
                right.add(topping[i]);
                count[topping[i]]--;
                if(count[topping[i]] == 0) left.remove(topping[i]);
                if(right.size() == left.size()) answer++;
            }

            return answer;
        }
    }
}
