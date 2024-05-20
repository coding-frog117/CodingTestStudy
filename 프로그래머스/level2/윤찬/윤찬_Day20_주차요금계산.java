package Programmers.lv2;

import java.util.*;
import java.util.stream.Collectors;

public class 윤찬_Day20_주차요금계산 {


    class Solution {
        public int[] solution(int[] fees, String[] records) {
            List<Integer> answer = new ArrayList<>();

            Map<String, Integer> car = new HashMap<>();
            Map<String, Integer> time = new HashMap<>();

            for(String record: records) {
                String[] s = record.split(" ");

                int getTime = getTime(s[0]);

                if(s[2].equals("IN")){
                    car.put(s[1], getTime);
                }else {
                    int in = car.getOrDefault(s[1], 0);
                    time.put(s[1], time.getOrDefault(s[1], 0) + (getTime - in));
                    car.remove(s[1]);
                }
            }

            for(String c: car.keySet()) {
                time.put(c, time.getOrDefault(c, 0) + (getTime("23:59") - car.get(c)));
            }

            for(String c : time.keySet().stream().sorted().collect(Collectors.toList())){
                int sum = time.get(c);

                if(sum <= fees[0]){
                    answer.add(fees[1]);
                }else {
                    int sub = sum - fees[0];
                    int mul = (int)Math.ceil(sub/(double)fees[2]);
                    answer.add(fees[1] + mul * fees[3]);
                }
            }

            return answer.stream().mapToInt(Integer::intValue).toArray();
        }

        public int getTime(String time) {
            int[] hm = Arrays.stream(time.split(":")).mapToInt(Integer::parseInt).toArray();
            return hm[0] * 60 + hm[1];
        }
    }
}
