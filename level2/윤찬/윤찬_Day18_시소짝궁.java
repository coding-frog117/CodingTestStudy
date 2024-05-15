package Programmers.lv2;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class 윤찬_Day18_시소짝궁 {
    class Solution {
        public long solution(int[] weights) {
            long answer = 0;

            Map<Integer, Integer> map = new HashMap<>();
            Map<Integer, Integer> w = new HashMap<>();

            // for(int i = 0; i < weights.length; i++) {
            //     for(int j = i + 1; j < weights.length; j++){
            //         if(isPair(weights[i], weights[j])) answer++;
            //     }
            // }

            for(int weight: weights) {
                //System.out.println("w.getOrDefault(weight, 0): " + w.getOrDefault(weight, 0));
                if(w.getOrDefault(weight, 0) != 0){
                    answer += w.getOrDefault(weight, 0);
                    w.put(weight, w.getOrDefault(weight, 0) + 1);
                    //System.out.println("same weight");
                    continue;
                }

                List<Integer> value = List.of(weight * 2, weight * 3, weight * 4);
                w.put(weight, w.getOrDefault(weight, 0) + 1);
                //set.add(weight);
                //List<Integer> value = List.of(weight * 2, weight * 3, weight * 4);


                for(int v: value) {
                    if(map.getOrDefault(v, -1) == -1){
                        map.put(v, map.getOrDefault(v, 0) + 1);
                    }else {
                        //System.out.println("v : " + v + ", " +map.getOrDefault(v, 0));
                        answer += map.getOrDefault(v, 0);
                        map.put(v, map.getOrDefault(v, 0) + 1);
                    }
                }

            }

            return answer;
        }

//     public boolean isPair(int a, int b) {
//         List<Integer> aList = List.of(a*2, a*3, a*4);
//         List<Integer> bList = List.of(b*2, b*3, b*4);
//         for(int aValue: aList){
//             for(int bValue: bList){
//                 if(aValue == bValue) return true;
//             }
//         }
//         return false;
//     }
    }
}
