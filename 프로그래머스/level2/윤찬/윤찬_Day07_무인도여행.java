package Programmers.lv2;

import java.util.*;

public class 윤찬_Day07_무인도여행 {

    class Solution {

        int[] dx = {0, 1, 0, -1};
        int[] dy = {-1, 0, 1, 0};
        int[][] map;
        boolean[][] visited;

        public int[] solution(String[] maps) {
            List<Integer> answer = new ArrayList<>();

            map = new int[maps.length][maps[0].length()];
            visited = new boolean[maps.length][maps[0].length()];

            for(int i = 0; i < maps.length; i++) {
                char[] c = maps[i].toCharArray();
                for(int j = 0; j < c.length; j++){
                    if(c[j] == 'X'){
                        visited[i][j] = true;
                        map[i][j] = 0;
                    }else {
                        map[i][j] = Integer.parseInt(String.valueOf(c[j]));
                    }
                }
            }

            // for(int[] m : map){
            //     for(int i: m){
            //         System.out.print(i + " ");
            //     }
            //     System.out.println();
            // }

            for(int i = 0; i < visited.length; i++){
                for(int j = 0; j < visited[0].length; j++) {
                    if(!visited[i][j]) {
                        answer.add(bfs(j, i));
                    }
                }
            }

            return answer.isEmpty() ? new int[]{-1} : answer.stream().sorted().mapToInt(Integer::intValue).toArray();
        }


        public int bfs(int x, int y) {
            Queue<int[]> queue = new LinkedList<>();
            queue.add(new int[]{x, y});
            visited[y][x] = true;
            int value = 0;
            while(!queue.isEmpty()) {
                int[] pos = queue.poll();
                //System.out.println("y,x " + pos[1] +"," + pos[0] +"add :" + map[pos[1]][pos[0]]);
                value += map[pos[1]][pos[0]];

                for(int i = 0; i < 4; i ++) {
                    int newX = pos[0] + dx[i];
                    int newY = pos[1] + dy[i];

                    if(newX >= 0 && newX < map[0].length && newY >=0 && newY < map.length){
                        if(!visited[newY][newX]) {
                            //System.out.println("newY : " + newY + "newX: "+ newX);
                            queue.add(new int[]{newX, newY});
                            visited[newY][newX] = true;
                        }
                    }

                }
            }

            return value;
        }
    }
}
