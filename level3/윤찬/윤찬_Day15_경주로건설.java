package Programmers.lv3;

import java.util.*;

public class 윤찬_Day15_경주로건설 {

    class Solution {
        int[][] maps;
        int[][] pos = new int[][] {
                {1, 0},
                {-1, 0},
                {0, 1},
                {0, -1}
        };
        boolean[][] visited;
        int n;
        int answer;
        public int solution(int[][] board) {
            answer = Integer.MAX_VALUE;
            maps = board;
            n = board.length;
            visited = new boolean[n][n];

            bfs();

            return answer;
        }

        public void bfs(){

            Queue<int[]> queue = new LinkedList<>();
            queue.add(new int[]{ 0, 0, -1, 0});
            visited[0][0] = true;

            while(!queue.isEmpty()) {
                int[] cur = queue.poll();

                if(cur[0] == n-1 && cur[1] == n - 1) {
                    answer = Math.min(answer, cur[3]);
                }

                for(int i = 0; i < pos.length; i++){
                    int[] p = pos[i];
                    int nextX = cur[1] + p[1];
                    int nextY = cur[0] + p[0];

                    if(nextX < 0 || nextX >= n || nextY < 0 || nextY >= n || maps[nextY][nextX] == 1){
                        continue;
                    }

                    if(!visited[nextY][nextX]){
                        if(cur[2] == -1 || i == cur[2]) {
                            queue.add(new int[] { nextY, nextX, i, cur[3] + 100});
                        }else {
                            queue.add(new int[] { nextY, nextX, i, cur[3] + 600});
                        }
                        visited[nextY][nextX] = true;
                    }

                }

            }



//         if(x == n -1 && y == n - 1) {
//             answer = Math.min(answer, price);
//             return;
//         }

//         for(int i = 0; i < pos.length; i++){
//             int[] p = pos[i];
//             int nextX = x + p[0];
//             int nextY = y + p[1];

//             if(nextX >= 0 && nextX < n && nextY >= 0 && nextY < n && maps[nextY][nextY] != 1) {
//                 if(!visited[nextY][nextX]){
//                     visited[nextY][nextX] = true;

//                     if(prev[0] == -1 || ((x == nextX) && (prev[0] == nextX)) || ((y == nextY) && (prev[1] == nextY)) ) {
//                         dfs(nextX, nextY, new int[] { x, y }, price + 100);
//                     }else {
//                         dfs(nextX, nextY, new int[] { x, y}, price + 600);
//                     }
//                     //visited[nextY][nextX] = false;
//                 }
//             }
//         }

        }

    }
}
