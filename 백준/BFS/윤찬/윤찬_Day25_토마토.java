package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class pb7576 {

    static int[][] maps;
    //static boolean[][] isFinish;
    static int[][] direction = new int[][]{
            {0, -1}, {0, 1}, {1, 0}, {-1, 0},
    };

    public static void main(String[] args) throws IOException {

        int answer = -1;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int M = input[0];
        int N = input[1];

        maps = new int[N][M];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < M; j++) {
                maps[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        bfs();

        boolean check = true;
        for (int[] map : maps) {
            for (int i : map) {
                if (i == 0) {
                    check = false;
                }
                answer = Math.max(answer, i);
            }
        }

        if (check) {
            System.out.println(answer - 1);
        } else {
            System.out.println(-1);
        }
    }

    private static void bfs() {
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < maps.length; i++) {
            for (int j = 0; j < maps[i].length; j++) {
                if (maps[i][j] == 1) {
                    queue.add(new int[]{i, j});
                }
            }
        }

        while (!queue.isEmpty()) {
            int[] q = queue.poll();

            for (int[] d : direction) {
                int dx = q[1] + d[1];
                int dy = q[0] + d[0];

                if (dx >= 0 && dx < maps[0].length && dy >= 0 && dy < maps.length && maps[dy][dx] == 0) {
                    maps[dy][dx] = maps[q[0]][q[1]] + 1;
                    queue.add(new int[]{dy, dx});
                }
            }

        }
    }


//    private static void dfs(int day) {
//        List<int[]> list = new ArrayList<>();
//
//        for(int i = 0; i < maps.length; i++) {
//            for(int j = 0; j < maps[i].length; j++) {
//                if(!isFinish[i][j] && maps[i][j] == 1) {
//                    isFinish[i][j] = true;
//                    for (int[] d : direction) {
//                        int dx = j + d[0];
//                        int dy = i + d[1];
//
//                        if (dx >= 0 && dx < maps[0].length && dy >= 0 && dy < maps.length && !isFinish[dy][dx]) {
//                            list.add(new int[]{dy, dx});
//                        }
//                    }
//                }
//            }
//        }
//
//        if(list.isEmpty()) {
//            boolean isAllFinish = true;
//            for(int i = 0; i < maps.length; i++) {
//                for(int j = 0; j < maps[i].length; j++) {
//                    if (!isFinish[i][j]) {
//                        isAllFinish = false;
//                        break;
//                    }
//                }
//            }
//
//            if(isAllFinish){
//                answer = day;
//            }else {
//                answer = -1;
//            }
//        }else {
//            for(int[] c : list) {
//                maps[c[0]][c[1]] = 1;
//            }
//            dfs(day + 1);
//        }
//    }
}
