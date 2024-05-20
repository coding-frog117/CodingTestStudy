package Programmers.lv3;

public class 윤찬_Day10_등굣길 {

    class Solution {
        public int solution(int m, int n, int[][] puddles) {
            int answer = 0;

            int[][] map = new int[n + 1][m + 1];

            for(int[] w : puddles) {
                map[w[1]][w[0]] = Integer.MAX_VALUE;
            }

            for(int i = 0; i <= m; i++) {
                map[0][i] = Integer.MAX_VALUE;
            }

            for(int i = 0; i <= n; i ++) {
                map[i][0] = Integer.MAX_VALUE;
            }

            map[1][1] = 1;
            for(int i = 1; i <= n; i++) {
                for(int j = 1; j <= m; j++){
                    if(i == 1 && j == 1) continue;

                    if(map[i][j] != Integer.MAX_VALUE) {
                        int up = map[i-1][j] != Integer.MAX_VALUE ? map[i-1][j] : 0;
                        int left = map[i][j - 1] != Integer.MAX_VALUE ? map[i][j - 1] : 0;
                        map[i][j] = (up + left) % 1_000_000_007;
                    }
                }
            }

            // for(int i = 1; i <= n; i++) {
            //     for(int j = 1; j <= m; j++){
            //         System.out.print(map[i][j] +" ");
            //     }
            //     System.out.println();
            // }

            return map[n][m];
        }
    }
}
