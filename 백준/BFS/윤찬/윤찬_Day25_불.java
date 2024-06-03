package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class pb4179 {

    static int[][] fire_maps;
    static int[][] maps;
    static int[][] direction = new int[][]{
            {0, -1}, {0, 1}, {1, 0}, {-1, 0},
    };

    public static void main(String[] args) throws IOException {
        int answer = Integer.MAX_VALUE;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        StringTokenizer st = new StringTokenizer(br.readLine());

        int row = Integer.parseInt(st.nextToken());
        int col = Integer.parseInt(st.nextToken());

        maps = new int[row][col];
        fire_maps = new int[row][col];

        for (int i = 0; i < row; i++) {
            String[] str = br.readLine().split("");
            for (int j = 0; j < col; j++) {
                if(str[j].equals("#")) {
                    maps[i][j] = -1;
                    fire_maps[i][j] = -1;
                }else if(str[j].equals("J")) {
                    maps[i][j] = 1;
                }else if(str[j].equals("F")) {
                    fire_maps[i][j] = 1;
                }
            }
        }

        bfs(maps);
        bfs(fire_maps);

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if(i == 0 || i == row - 1 || j == 0 || j == col - 1) {
                    if(maps[i][j] != -1 && maps[i][j] < fire_maps[i][j]) {
                        answer = Math.min(answer, maps[i][j]);
                    }
                }
            }
        }

        if(answer == Integer.MAX_VALUE) {
            System.out.println("IMPOSSIBLE");
        }else{
            System.out.println(answer);
        }

    }


    private static void bfs(int[][] m) {
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < m.length; i++) {
            for (int j = 0; j < m[i].length; j++) {
                if (m[i][j] == 1) {
                    queue.add(new int[]{i, j});
                }
            }
        }

        while (!queue.isEmpty()) {
            int[] q = queue.poll();

            for (int[] d : direction) {
                int dx = q[1] + d[1];
                int dy = q[0] + d[0];

                if (dx >= 0 && dx < m[0].length && dy >= 0 && dy < m.length && m[dy][dx] == 0) {
                    m[dy][dx] = m[q[0]][q[1]] + 1;
                    queue.add(new int[]{dy, dx});
                }
            }

        }
    }
}
