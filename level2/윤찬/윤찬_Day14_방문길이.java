package Programmers.lv2;

import java.util.*;

public class 윤찬_Day14_방문길이 {

    class Solution {
        public int solution(String dirs) {

            Map<Character, int[]> map = new HashMap<>();

            map.put('U', new int[]{1, 0});
            map.put('D', new int[]{-1, 0});
            map.put('R', new int[]{0, 1});
            map.put('L', new int[]{0, -1});

            Set<String> set = new HashSet<>();

            int start_x = 5;
            int start_y = 5;

            for(char c : dirs.toCharArray()){
                int[] direction = map.get(c);
                int dy = start_y + direction[0];
                int dx = start_x + direction[1];

                if(validation(dx, dy)){
                    set.add(start_x + " " + start_y + " " + dx + " " + dy);
                    set.add(dx + " " +  dy + " " + start_x + " " + start_y);
                    start_x = dx;
                    start_y = dy;
                }
            }

            return set.size() / 2;
        }

        public boolean validation(int x,int y) {
            return x >=0 && x <= 10 && y >= 0 && y <= 10;
        }
    }

}
