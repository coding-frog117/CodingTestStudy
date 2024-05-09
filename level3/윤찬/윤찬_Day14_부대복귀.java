package Programmers.lv3;

import java.util.*;

public class 윤찬_Day14_부대복귀 {

    class Solution {

        List<Integer>[] list;
        int[] dis;

        public int[] solution(int n, int[][] roads, int[] sources, int destination) {
            int[] answer = new int[sources.length];
            list = new ArrayList[n+1];
            for(int i = 0; i <= n; i++) {
                list[i] = new ArrayList<>();
            }

            for(int[] road: roads) {
                int a = road[0];
                int b = road[1];
                list[a].add(b);
                list[b].add(a);
            }


            dis = new int[n + 1];
            Arrays.fill(dis, Integer.MAX_VALUE);
            bfs(destination);

            for(int i = 0; i < sources.length; i++) {
                answer[i] = dis[sources[i]] == Integer.MAX_VALUE ? -1 : dis[sources[i]];
            }

            return answer;
        }

        public void bfs(int start) {
            dis[start] = 0;

            Queue<Integer> queue = new LinkedList<>();
            queue.add(start);

            while(!queue.isEmpty()) {

                int node = queue.poll();

                for(int next: list[node]){

                    if(dis[next] > dis[node] + 1) {
                        dis[next] = dis[node] + 1;
                        queue.add(next);
                    }
                }

            }
        }
    }
}
